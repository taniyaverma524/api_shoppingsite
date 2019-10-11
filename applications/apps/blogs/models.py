from django.db import models
from django.utils.safestring import mark_safe

from apps.users.models import User
import re
import random


class  Blog(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    email=models.EmailField(max_length=500)
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32,unique=True)
    body = models.TextField()
    image = models.CharField(max_length=225, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, blank=True, related_name='post_like')
    updated=models.DateTimeField(auto_now=True , auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False , auto_now_add=True)
    def save(self, *args, **kwargs):
        print(self.slug == "")
        print(self.email,self.email == "")
        slug1=self.title.lower()
        if self.slug == "" :
            slug2 = re.sub(r'\W', "", slug1)
            self.slug = re.sub(r'\d*', "", slug2) + str(random.randint(1, 999))
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def half(self):
        return self.body[:150] + "[....]"
    # def get_markdown(self):
    #     content=self.body
    #     markdown_text=markdown(content)
    #     return mark_safe(markdown_text)
    class Meta:
        unique_together =( 'title' , 'user' )

class Comment(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    comment = models.CharField(max_length=512)
    name=models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    email = models.EmailField()

    def __str__(self):
        return self.blog.title

    class Meta:
        ordering = ('-created',)





