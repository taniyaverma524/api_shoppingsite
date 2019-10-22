from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField
from apps.blogs.models import Blog, Comment
from django.forms.models import model_to_dict


blog_detail_url = HyperlinkedIdentityField(
    view_name='blog-api:detail',
    lookup_field='slug'
)


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
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
    url = blog_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='blog-api:delete',
        lookup_field='slug'
    )
    user = SerializerMethodField()

    class Meta:
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

    def get_user(self, obj):
        return str(obj.user.username)


class PostDetailSerializer(serializers.ModelSerializer):
    url = blog_detail_url
    user = SerializerMethodField()

    # markdown = SerializerMethodField()
    class Meta:
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

    def get_user(self, obj):
        return str(obj.user.username)
    # def get_markdown(self,obj):
    #     pass


comment_url = HyperlinkedIdentityField(
    view_name='blog-api:comment_detail',
    lookup_field='id'
)

class CommentSerializer(serializers.ModelSerializer):
    details_url = comment_url
    class Meta:
        model = Comment
        fields = [
            'comment',
            'name',
            'email',
            'details_url',
        ]

class CommentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'blog',
            'comment',
            'name',
            'email',

        ]

class BlogCommentSerializer(serializers.ModelSerializer):
    comment=SerializerMethodField()
    class Meta:
        model = Blog
        # fields = "__all__"
        fields =[
            'id',
            'title',
            'body',
            'name',
            'comment',
        ]
    def get_comment(self,obj):

        # set_=[]
        blog_objects=Comment.objects.filter(blog=obj)
        # for i in blog_objects:
        #     # details_url = HyperlinkedIdentityField(
        #     #     view_name='blog-api:comment_detail',
        #     #     lookup_field='i.id'
        #     # )
        #     set_.append({'comment':i.comment,'email':i.email,
        #                  # 'url':model_to_dict(details_url)
        #                  })
        comments=CommentSerializer(blog_objects,many=True,context={'request': self.context.get('request', None)}).data
        return comments
        # return 0


class CommentCreateSerializer(serializers.ModelSerializer):
    print("helllooo")
    class Meta:
        model = Comment
        # fields=['comment']

        fields="__all__"