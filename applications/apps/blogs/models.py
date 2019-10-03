from django.db import models
from apps.users.models import User




class  Blog(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32,unique=True)
    body = models.TextField()
    image = models.CharField(max_length=225, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, blank=True, related_name='post_like')
    updated=models.DateTimeField(auto_now=True , auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False , auto_now_add=True)


    def __str__(self):
        return self.title

    def half(self):
        return self.body[:150] + "[....]"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    comment = models.CharField(max_length=512)
    name=models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    email = models.EmailField()

    def __str__(self):
        return self.blog.title

    class Meta:
        ordering = ('-created',)





