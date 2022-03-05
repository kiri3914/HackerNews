from rest_framework import serializers
from news.models import (
    Post,
    Comment,
    User
)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'comment', 'created_on', 'updated_on', 'parent']

        extra_kwargs = {
            'author': {'read_only': True},
            'parent': {'read_only': True},
            'children': {'read_only': True},
            'created_on': {'read_only': True},
            'updated_on': {'read_only': True}
        }

        def get_child_comments(self, obj):
            serializer = CommentSerializer(instance=obj.get_children(), many=True)
            return serializer.data


class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'link', 'points', 'created_at', 'slug', 'post_comment')

        extra_kwargs = {
            'author': {'read_only': True},
            'created_at': {'read_only': True},
            'slug': {'read_only': True},
            'post_comment': {'read_only': True}
        }
