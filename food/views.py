from abc import ABC
import re
from django.http.response import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.forms import ModelForm, TextInput, EmailInput, NumberInput
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied, BadRequest
from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.utils.text import slugify
from django.db.models import Q
from django.db import models
from django import forms

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework import status


from hitcount.views import HitCountDetailView
from food.serializer import FoodSerializer
from food.forms import FoodForm
from food.models import Food


# 작동 문제 없음
class FoodList(ListView):
    model = Food
    template_name = 'food/food_list.html'
    ordering = '-pk'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FoodList, self).get_context_data()
        page_size = 5
        start_index = int((context['page_obj'].number - 1) / page_size) * page_size
        end_index = min(start_index + page_size, len(context['paginator'].page_range))
        context['page_range'] = context['paginator'].page_range[start_index: end_index]
        context['ranks'] = CustomUser.objects.filter(comment_count__gt=0).order_by('-heart_point')[:10]
        if Food.objects.all():
            pop_food = Food.objects.order_by("-hit_count_generic__hits")[0]
            if pop_food:
                context['pop_food'] = pop_food
            hot_food = Food.objects.order_by("-comment")[0]
            if hot_food:
                context['hot_food'] = hot_food
            expensive_food = Food.objects.order_by("-heart_point")[0]
            if expensive_food:
                context['expensive_question'] = expensive_food
            if Food.objects.filter(who_chosen=None):
                difficult_food = Food.objects.filter(who_chosen=None).order_by("-post_date")[0]
                if difficult_food:
                    context['difficult_food'] = difficult_food
        return context


# 작동 문제 없음
class FoodDetail(HitCountDetailView):
    model = Food
    template_name = 'food/food_detail.html'
    count_hit = True
    context_object_name = "food"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(FoodDetail, self).get_context_data()
    #     context['comment_form'] = CommentForm
    #     return context


# 작동 문제 없음
class FoodCreate(LoginRequiredMixin, CreateView, ABC):
    model = Food
    form_class = FoodForm
    template_name = 'food/food_form.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.user_id = current_user
            response = super(FoodCreate, self).form_valid(form)
        else:
            return redirect('/food')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FoodCreate, self).get_context_data()
        return context


# 작동 문제 없음
class FoodUpdate(LoginRequiredMixin, UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'food/food_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user_id:
            return super(FoodUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.user_id = current_user
            response = super(FoodUpdate, self).form_valid(form)
        else:
            return redirect('/food')


# 검색 기능
class FoodSearch(FoodList):
    paginate_by = 8

    def get_queryset(self):
        q = self.kwargs['q']
        food_list = Food.objects.filter(
            Q(food_title__contains=q)
            | Q(food_desc__contains=q)
            | Q(category_id__slug__contains=q)
        ).distinct()
        return food_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FoodSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search : {q} ({self.get_queryset().count()})'
        return context
