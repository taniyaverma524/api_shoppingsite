from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    gender = models.CharField(choices=GENDER_CHOICE, max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'

        default_permissions = ()
        permissions = (
            # Users related permissions
            ('view_user', 'Can view users.'),
            ('list_user', 'Can list users.'),
            ('add_user', 'Can add users.'),
            ('edit_user', 'Can edit users.'),
            ('delete_user', 'Can delete users.'),
            ('csv_for_user', 'Can download csv for users.'),

            # More Permissions
        )

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']