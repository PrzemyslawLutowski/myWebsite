from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response

from api import serializers
from blog import models as blog


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = serializers.GroupSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    # queryset = blog.BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer

    def get_queryset(self):
        queryset = blog.BlogPost.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = serializers.BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = serializers.BlogPostSerializer(instance)
        return Response(serializer.data)


