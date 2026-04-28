from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog import models as blog


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog.BlogPost
        fields = ('title',
                  'slug',
                  'content',
                  'publish',
                  'status',
                  'author',
                  )

class BlogPostMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog.BlogPost
        fields = ('title',
                  'status',
                  'author',
                  )
