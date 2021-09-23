from django.contrib import admin
from .models import Comment, Food, User #클래스 이름 모름

# Register your models here.
admin.site.register(Food)
admin.site.register(User)
admin.site.register(Comment)