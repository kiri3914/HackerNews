from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSetMixin
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

from .permissions import (
    IsActive,
    IsAuthorOrIsAuthenticated
)
from .models import (
    Post,
    Comment
)
from .serializers import (
    PostSerializer,
    CommentSerializer
)


class PostViewSet(ModelViewSet, mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'link')

    def get_queryset(self):
        return Post.objects.filter(author_id=self.request.user)

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = Post.objects.all().order_by('created_at')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('', 'link')

    def get_queryset(self):
        return Comment.objects.filter(author_id=self.request.user)

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = Comment.objects.all().order_by('created_on')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)


