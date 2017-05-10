from rest_framework import serializers

from authentication.serializers import UserSerializer, UserShortSerializer, Base64ImageField
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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'url')


class KeywordSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=False)

    class Meta:
        model = Keyword
        fields = ('tag',)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    author = UserShortSerializer(many=False)
    likes = LikeSerializer(many=True)
    keywords = KeywordSerializer(many=True)
    image = Base64ImageField(
        max_length=None, use_url=True,
        allow_null=True, required=False,
    )

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'publish_date', 'author', 'comments', 'likes', 'image', 'keywords',)


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
    image = Base64ImageField(
        max_length=None, use_url=True, required=False, allow_null=True
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'short_description', 'image',)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
