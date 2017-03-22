from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content')

class PostShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'short_description', 'publish_date', 'author')
