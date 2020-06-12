from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from .models import Post

# Create your views here.

class Postview(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class Testview(APIView):

    # permission_classes = (IsAuthenticated,)

    # def get(self, request, *args, **kwargs):
    #     qs = Post.objects.all()
    #     fr = qs.last()
    #     # serializer = PostSerializer(qs, many=True)
    #     serializer = PostSerializer(fr)
    #     return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)