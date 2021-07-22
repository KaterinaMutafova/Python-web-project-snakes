from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Python(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(
        upload_to='media_snake_images',
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    @property
    def count_pythons(self):
        pass



