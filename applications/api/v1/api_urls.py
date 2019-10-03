from django.urls import path, include
from api.v1.apiview.blog_view import PostListApiView ,PostDetailAPIView \
    ,PostUpdateAPIView ,PostDeleteAPIView

urlpatterns = [
    path('blog_list/',PostListApiView.as_view()),
    path('blog_detail/<slug:slug>/',PostDetailAPIView.as_view()),
    path('blog_update/<slug:slug>/', PostUpdateAPIView.as_view()),
    path('blog_delete/<slug:slug>/', PostDeleteAPIView.as_view()),
]
