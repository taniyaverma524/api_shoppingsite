from django.db.models import Q
from rest_framework.filters import (
    SearchFilter, OrderingFilter,
)
from django.http import Http404
from rest_framework.views import APIView
from api.v1.paginations import PostLimitOffsetPagination, PostPageNumberPagination

from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveAPIView, UpdateAPIView,
    CreateAPIView, RetrieveUpdateAPIView
)
from apps.blogs.models import Blog, Comment
from api.v1.serializers.blog_serializer import (
    PostDetailSerializer, PostListSerializer,
    PostCreateUpdateSerializer, CommentSerializer
, BlogCommentSerializer,
    CommentDetailSerializer)
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from api.v1.permissions import IsOwnerOrReadOnly


class PostCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(email=self.request.user.email, user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(email=self.request.user.email, user=self.request.user)



class PostDeleteAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'



class PostListApiView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['body', 'user__first_name', 'user__last_name', 'name']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Blog.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(body__icontains=query) |
                Q(name__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list


class CommentDetailsApiView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'id'



class CommentListApiView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog', 'comment', 'name', 'email']
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(blog__icontains=query) |
                Q(comment__icontains=query) |
                Q(name__icontains=query) |
                Q(email__first_name__icontains=query)
            )
        return queryset_list


class BlogCommentApiView(APIView):
    def get_object(self,id):
        try:
            return Blog.objects.get(id=id)
        except :
            return Http404
    def get(self,request,id,format=None):
        blog_object=self.get_object(id)
        blog_serializer=BlogCommentSerializer(blog_object)
        return Response(blog_serializer.data)





