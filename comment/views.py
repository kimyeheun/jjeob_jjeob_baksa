from django.shortcuts import render
from django.views.generic import ListView, DetailView

from comment.models import Comment
from comment.forms import CommentForm

# Create your views here.

class CommentList():
    model = Comment


class CommentDetail(DetailView):
    model = Comment
    template_name = 'comment_details.html'

class CommentCreate():
    model = Comment
    template_name = 'comment_create.html'
