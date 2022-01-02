from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Food(models.Model):
    food_id = models.IntegerField(null=True)
    # user_id = models.ForeignKey(on_delete=True, to=User)
    # category_id = models.ForeignKey(on_delete=True, to=User)

    heart_vote = models.BooleanField(default=False)

    food_date = models.DateTimeField(auto_now=True)
    modify_date = models.DateTimeField(auto_now=True)
    food_pic = models.ImageField(upload_to='food_pics', null=True, blank=True) # pip install pillow 해야함
    food_desc = models.CharField(max_length=2000)
    food_title = models.CharField(max_length=100, null=True)
