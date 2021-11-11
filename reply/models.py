from django.db import models

class reply(models.Model):
    user_id = models.ForeignKey(on_delete=models.SET_NULL)
    post_date = models.DateField()
    modify_date = models.DateField()
    reply_desc = models.TextField()
    
# Create your models here.
