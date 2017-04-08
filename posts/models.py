from django.db import models

# Create your models here.
from authentication.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    short_description = models.TextField(null=False)
    content = models.TextField(null=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=False)
    author = models.ForeignKey(User, null=False, related_name='posts', on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField(null=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=False)
    author = models.ForeignKey(User, null=False, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, related_name='comments', on_delete=models.CASCADE)

class Like(models.Model):
    post = models.ForeignKey(Post, null=False, related_name='likes', on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, related_name='likes', on_delete=models.CASCADE)