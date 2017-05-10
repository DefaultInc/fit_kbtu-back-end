from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from authentication.models import User
from authentication.serializers import UserSerializer
from posts.paginators import StandardResultsSetPagination
from .models import Post, Comment, Keyword, Tag
from .serializers import PostSerializer, PostShortSerializer, CommentSerializer, CommentCreateSerializer, \
    LikeSerializer, LikeCreateSerializer, PostCreateSerializer, KeywordSortSerializer, TagSerializer


# Create your views here.
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def post_create(request):
    """
    create a new post
    """

    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['author'] = request.user.id
        serializer = PostCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def comment_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # author is defined by his JWT token, improce readability
        data['author'] = request.user.id
        serializer = CommentCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def like_exists(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        post = get_object_or_404(Post, id=data['post'])
        likes = post.likes.filter(author=data['author'])
        print(likes)
        if likes.exists():
            likes[0].delete()
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def like_post(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['author'] = request.user.id
        # checking if user has like on this post
        post = get_object_or_404(Post, id=data['post'])
        post_author_likes = post.likes.filter(author=data['author'])
        # dislike
        if post_author_likes.exists():
            post_author_likes[0].delete()
            return JsonResponse(data)
        else:
            serializer = LikeCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


class PostList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostShortSerializer
    pagination_class = StandardResultsSetPagination


class TagList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    model = Tag
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostByTag(generics.ListAPIView):
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination
    serializer_class = KeywordSortSerializer

    def get_queryset(self):
        keywords = Keyword.objects.filter(tag_id=int(self.kwargs['pk']))
        for keyword in keywords:
            if keywords.filter(post_id=keyword.id).count() > 1:
                keywords.exclude(keyword)
        return keywords


class PostByTags(generics.ListAPIView):
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination
    serializer_class = KeywordSortSerializer

    def get_queryset(self):
        ids = self.request.query_params.get('ids', None)
        if ids is not None:
            ids = [int(x) for x in ids.split(',')]
            keywords = Keyword.objects.filter(tag_id__in=ids)
            if keywords.__len__() < 2:
                for keyword in keywords:
                    print(keyword)
                    if keywords.filter(post_id=keyword.id).count() > 1:
                        keywords.exclude(keyword)
        else:
            keywords = Keyword.objects.all()
        return keywords


def post_detail(request, pk):
    """
    Retrieve, update or delete a post.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)
