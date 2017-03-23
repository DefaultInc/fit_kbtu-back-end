from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    short_description = models.TextField(null=False)
    content = models.TextField(null=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=False)
    author = models.CharField(max_length=50, null=False)
