from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField,SerializerMethodField
from apps.blogs.models import Blog, Comment

blog_detail_url = HyperlinkedIdentityField(
    view_name='blog-api:detail',
    lookup_field='slug'
    )

class PostCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta :
        model = Blog
        fields = [
            # 'id',
            'name',
            'title',
            # 'slug',
            'body',
            'date',
        ]


class PostListSerializer(serializers.ModelSerializer):
    url=blog_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='blog-api:delete',
        lookup_field='slug'
    )
    user=SerializerMethodField()
    class Meta :
        model = Blog
        fields = [
            'title',
            'url',
            # 'slug',
            'body',
            'updated',
            'email',
            'user',
            'delete_url',
        ]
    def get_user(self,obj):
        return str(obj.user.username)

class PostDetailSerializer(serializers.ModelSerializer):
    url=blog_detail_url
    user= SerializerMethodField()
    # markdown = SerializerMethodField()
    class Meta :
        model = Blog
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'body',
            'url',
            'image',
        ]
    def get_user(self,obj):
        return str(obj.user.username)
    # def get_markdown(self,obj):
    #     pass


class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model=Comment
        fields=[
            'blog',
            'comment',
            'name',
            'email',
        ]


class CommentChildSerializer(serializers.ModelSerializer):
    class Meta :
        model=Comment
        fields=[
            'id',
            'comment',
            'name',
            'email',
        ]

class CommentDetailSerializer(serializers.ModelSerializer):
    replies=SerializerMethodField()
    class Meta :
        model=Comment
        fields=[
            'id',
            'blog',
            'comment',
            'name',
            'email',
            'replies',
        ]
    def get_replies(self,obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.childrend(),many=True).data
        return None


