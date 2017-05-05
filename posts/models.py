from django.db import models

# Create your models here.
from authentication.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False)
    short_description = models.TextField(null=False)
    content = models.TextField(null=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=False)
    author = models.ForeignKey(User, null=False, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(null=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=False)
    author = models.ForeignKey(User, null=False, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Like(models.Model):
    post = models.ForeignKey(Post, null=False, related_name='likes', on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, related_name='likes', on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    users = models.ManyToManyField(User, related_name='tags')

    def __str__(self):
        return self.name


class Keyword(models.Model):
    tag = models.ForeignKey(Tag, related_name='keywords')
    post = models.ForeignKey(Post, related_name='keywords')

    class Meta:
        unique_together = (('tag', 'post'))

    def __str__(self):
        return str(self.id)
