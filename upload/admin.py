from django.contrib import admin

from .models import Uploaded_file, Uploaded_image


class FilesAdmin(admin.ModelAdmin):
    fields = ['user', 'file_url', "media", "thumbnail"]


class ImagesAdmin(admin.ModelAdmin):
    fields = ['user', 'file_url', "media", "thumbnail"]


admin.site.register(Uploaded_file, FilesAdmin)
admin.site.register(Uploaded_image, ImagesAdmin)
