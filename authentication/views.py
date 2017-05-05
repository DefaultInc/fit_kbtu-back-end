from django.http import JsonResponse, HttpResponse, Http404

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from authentication.models import User
from authentication.serializers import UserSerializer
from posts.models import Post


def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serialized = UserSerializer(data=data)
        if serialized.is_valid():
            UserSerializer.create(serialized, data)
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', ])
@authentication_classes([JSONWebTokenAuthentication, ])
@permission_classes([IsAuthenticated, ])
def user_profile(request):
    try:
        user = request.user
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)