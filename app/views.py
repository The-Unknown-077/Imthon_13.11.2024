from django.shortcuts import render
from rest_framework import generics
from .models import BlogDESC, Kategoriya
from .serializers import BlogSerializer, KategoriyaSerializer

class BlogMaqolaList(generics.ListAPIView):
    queryset = BlogDESC.objects.all()
    serializer_class = BlogSerializer

class BlogMaqolaDetail(generics.RetrieveAPIView):
    queryset = BlogDESC.objects.all()
    serializer_class = BlogSerializer

class KategoriyaList(generics.ListAPIView):
    queryset = Kategoriya.objects.all()
    serializer_class = KategoriyaSerializer



