from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.parsers import JSONParser

from authentication.serializers import UserSerializer


def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serialized = UserSerializer(data=data)
        if serialized.is_valid():
            UserSerializer.create(serialized, data)
            # User.objects.create_user(
            #     serialized.init_data['username'],
            #     serialized.init_data['password']
            # )
            return JsonResponse(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialized._errors, status=status.HTTP_400_BAD_REQUEST)