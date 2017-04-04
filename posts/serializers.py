from rest_framework import serializers

from authentication.serializers import UserSerializer
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'publish_date', 'author')

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    author = UserSerializer(many=False)
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'publish_date', 'author', 'comments')

class PostShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'short_description', 'publish_date', 'author')
