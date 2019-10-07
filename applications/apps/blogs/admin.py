from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from apps.blogs.forms import BlogCategoryForm
from apps.blogs.models import Blog ,Comment





class CommentInlines(admin.TabularInline):
    model = Comment
    # readonly_fields = ("email", "comment", 'name')
    extra = 0


def get_image_preview(obj):
    if obj.pk and obj.image :
        return mark_safe('<img src="%s" width="150" height="150" />' % (obj.image)
                         )

    return _("(choose a picture and save and continue editing to see the preview)")

get_image_preview.short_description = _("Picture Preview")


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = BlogCategoryForm
    fields = ['name', 'title','slug',   'body', 'image','email','user',

              'like','select_image', get_image_preview]
    readonly_fields = ['image', get_image_preview]
    inlines = [CommentInlines]




admin.site.register(Blog, BlogAdmin)










