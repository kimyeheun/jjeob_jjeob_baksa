from django.db import models

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Food, related_name="comments", on_delete = models.CASCADE) #if post is deleted, automatically delete the comment
    user_id = models.CharField(max_length = 255)
    comment_desc = models.TextField()
    comment_date = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' %(self.post.title, self.user_id)