from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    date_of_birth = models.DateTimeField()
    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )



