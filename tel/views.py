from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from posts.paginators import StandardResultsSetPagination
from tel.models import Telephone
from tel.serializers import TelephoneSerializer, TelephoneCreateSerializer

class TelList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    model = Telephone
    queryset = Telephone.objects.all().order_by('user_name')
    serializer_class = TelephoneSerializer
    pagination_class = StandardResultsSetPagination

def tel_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TelephoneCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def tel_detail(request, pk):
    try:
        telephone = Telephone.objects.get(pk=pk)
    except Telephone.DoesNotExist:
        return Telephone(status=404)

    if request.method == 'GET':
        serializer = TelephoneSerializer(telephone)
        return JsonResponse(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TelephoneSerializer(telephone, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        telephone.delete()
        return HttpResponse(status=204)