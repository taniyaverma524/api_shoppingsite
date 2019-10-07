from django import forms
from apps.blogs.models import Blog
import random
from django.conf import settings
from utils import make_dir ,image_upload_handler



class BlogCategoryForm(forms.ModelForm):

    select_image = forms.FileField(required=False)



    class Meta:
        model = Blog
        fields = "__all__"

    def save(self, commit=True):
        extra_field = self.cleaned_data.get('select_image', None)
        if extra_field:
            rndm = random.randint(100000, 9999999)
            upload_dir = make_dir(
                settings.MEDIA_ROOT + settings.CUSTOM_DIRS.get('BLOGIMAGE_DIR') + '/' + str(
                    rndm) + '/'
            )
            file_name = image_upload_handler(extra_field, upload_dir)
            image = settings.MEDIA_URL + settings.CUSTOM_DIRS.get(
                'BLOGIMAGE_DIR') + '/' + str(rndm) + '/' + file_name
            self.instance.image = image


        return super(BlogCategoryForm, self).save(commit=commit)

