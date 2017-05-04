from django.contrib import admin
from .models import Post, Comment, Like, Tag, Keyword

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(Keyword)
