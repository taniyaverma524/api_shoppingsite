from rest_framework.generics import ListAPIView ,DestroyAPIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView ,UpdateAPIView
from apps.blogs.models import Blog
from api.v1.serializers.blog_serializer import PostDetailSerializer ,PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostListApiView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostListSerializer





 


