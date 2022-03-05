from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    title = models.TextField()
    link = models.URLField(max_length=1000, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    points = models.ManyToManyField(User, null=True, blank=True, related_name='points' )
    slug = AutoSlugField(populate_from='title', default=None, unique=True)

    def __str__(self):
        return self.title

    def get_points(self):
        return (self.points.count() + 1)

    def get_user_voted(self):
        return self.points.values_list('username', flat=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    @property
    def comment_count(self):
        return self.comment_set.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_to_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    comment = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="comment_parent", on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='comment', default=None, unique=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
