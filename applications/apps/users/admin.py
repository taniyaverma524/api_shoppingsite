from django.contrib import admin
from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['username','email'
                       ,'password','is_email_verified']
    list_display = ['username','is_email_verified']
admin.site.register(User,UserAdmin)

