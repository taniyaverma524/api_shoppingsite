from rest_framework import serializers
from apps.blogs.models import Blog




class PostListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Blog
        fields = [
            'title',
            'slug',
            'body',
            'updated',
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta :
        model = Blog
        fields = [
            'id',
            'title',
            'slug',
            'body',
        ]




