from django.db import models
from django.contrib.auth.models import User, AbstractUser


# TODO from django.core.files.storage import FileSystemStorage
# TODO fs = FileSystemStorage(location='/media/photos')


class Profile(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=128, blank=True, null=True)


class Picture(models.Model):
    title = models.CharField(max_length=32, blank=False)
    image = models.ImageField()  # TODO storage = fs
    description = models.TextField(default="", blank=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
