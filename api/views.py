from .serializers import *
from .models import *
from .utils import ObjectMixin

from rest_framework import viewsets


class PostViewSet(ObjectMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    model = Post
    serializer = PostSerializer


class CommentViewSet(ObjectMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    model = Comment
    serializer = CommentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(ObjectMixin, viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    model = Follow
    serializer = FollowSerializer
