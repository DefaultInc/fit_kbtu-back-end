from rest_framework import serializers

from authentication.serializers import UserSerializer, UserShortSerializer
from .models import Post, Comment, Like, Keyword, Tag


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('content', 'publish_date', 'author', 'post',)


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'publish_date', 'author', 'post',)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class LikeSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(many=False)

    class Meta:
        model = Like
        fields = ('author',)


class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('author', 'post',)

    def create(self, validated_data):
        return Like.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    author = UserShortSerializer(many=False)
    likes = LikeSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'publish_date', 'author', 'comments', 'likes', 'image',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)


class KeywordSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=False)

    class Meta:
        model = Keyword
        fields = ('tag',)


class PostShortSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(many=False)
    likes = LikeSerializer(many=True)
    keywords = KeywordSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'short_description', 'publish_date',
            'author', 'likes', 'comments', 'image', 'keywords',
        )


class KeywordSortSerializer(serializers.ModelSerializer):
    post = PostShortSerializer(many=False)

    class Meta:
        model = Keyword
        fields = ('post',)


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'short_description')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
