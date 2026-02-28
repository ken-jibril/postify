from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Post, Category, Tag
from .serializers import (
    PostSerializer,
    UserSerializer,
    CategorySerializer,
    TagSerializer
)
from .permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'author', 'published_date', 'tags']
    search_fields = ['title', 'content', 'author__username', 'tags__name']
    ordering_fields = ['published_date', 'created_date']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False)
    def by_category(self, request):
        category_id = request.query_params.get('category')
        posts = Post.objects.filter(category_id=category_id)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def by_author(self, request):
        author_id = request.query_params.get('author')
        posts = Post.objects.filter(author_id=author_id)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer