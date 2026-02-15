from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Category, Tag
from .serializers import PostSerializer, UserSerializer, CategorySerializer, TagSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, url_path='category/(?P<category_id>[^/.]+)')
    def by_category(self, request, category_id=None):
        posts = Post.objects.filter(category_id=category_id)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path='author/(?P<author_id>[^/.]+)')
    def by_author(self, request, author_id=None):
        posts = Post.objects.filter(author_id=author_id)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer