from rest_framework import serializers

from authentication.serializers import UserSerializer, UserShortSerializer
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('content', 'publish_date', 'author')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'publish_date', 'author', 'post')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    author = UserShortSerializer(many=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'publish_date', 'author', 'comments')


class PostShortSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(many=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'short_description', 'publish_date', 'author')
