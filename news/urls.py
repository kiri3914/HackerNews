from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    PostViewSet,
    CommentViewSet
)

router = DefaultRouter()

router.register('post', PostViewSet, basename='Post')
router.register('comment', CommentViewSet, basename='Comment')

urlpatterns = []
urlpatterns += router.urls
