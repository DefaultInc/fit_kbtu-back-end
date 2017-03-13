from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)
    content = models.CharField(max_length=256, blank=True, null=True)