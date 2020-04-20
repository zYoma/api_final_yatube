from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Follow
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


class ObjectMixin():
    model = None
    serializer = None

    def list(self, request, post_id=None):
        group = request.GET.get('group')
        search = request.GET.get('search')
        if post_id:
            obj = self.model.objects.filter(post=post_id)
        elif group:
            obj = self.model.objects.filter(group=group)
        elif search:
            obj = self.model.objects.filter(
                Q(following__username=search) | Q(user__username=search))
            print(obj)
        else:
            obj = self.model.objects.all()
        serializer = self.serializer(obj, many=True)
        return Response(serializer.data)

    def create(self, request, post_id=None):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():

            if request.path == '/api/v1/follow/':
                following = request.POST.get('following')
                user_following_list = Follow.objects.filter(
                    user=request.user).values_list('following__username', flat=True)
                if not following or following in user_following_list:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    following_user = get_object_or_404(
                        User, username=following)
                    serializer.save(user=request.user,
                                    following=following_user)
            else:
                serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, post_id=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None, post_id=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.serializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, post_id=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
