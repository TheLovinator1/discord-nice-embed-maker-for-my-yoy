from django import forms

from upload.models import Uploaded_file, Uploaded_image


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Uploaded_image
        fields = ('media',)


class FilesForm(forms.ModelForm):
    class Meta:
        model = Uploaded_file
        fields = ('media',)
