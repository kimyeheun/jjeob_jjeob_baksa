from rest_framework.routers import DefaultRouter
from rest_framework import routers

from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.FoodList.as_view(), name="food_main"),
    path('<int:pk>/', views.FoodDetail.as_view(), name='res'),
    path('create_food/', views.FoodCreate.as_view()),
    path('update_food/<int:pk>', views.FoodUpdate.as_view(), name="food_update"),
    path('food/search/', views.FoodUpdate.as_view(), name="food_search_base"),
    path('food/search/<str:q>/', views.FoodSearch.as_view(), name="food_search"),
    path('food/search/<str:q>/<str:pk>', views.FoodDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
