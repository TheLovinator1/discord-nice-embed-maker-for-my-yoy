from django.contrib.auth.models import User
from django.db import models


class Uploaded_file(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    file_url = models.URLField(blank=True)
    media = models.FileField(upload_to=f'files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to=f'thumbnails/', blank=True)


class Uploaded_image(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    file_url = models.URLField(blank=True)
    media = models.ImageField(upload_to=f'files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to=f'thumbnails/', blank=True)
