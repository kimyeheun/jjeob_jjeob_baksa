from django.urls import path, include
from .views import CommentCreate

urlpatterns = [
    path('', CommentCreate.as_view(), name = "home"),

    ]
