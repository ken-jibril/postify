from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, PostViewSet, CategoryViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
