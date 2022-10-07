from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from upload.models import Uploaded_file, Uploaded_image
from .forms import FilesForm, ImagesForm


def upload_files(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'discord_embed/index.html')
    else:
        form = FilesForm()
    return render(request, 'discord_embed/upload_files.html', {
        'form': form
    })


def upload_images(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'discord_embed/index.html')
    else:
        form = ImagesForm()
    return render(request, 'discord_embed/upload_images.html', {
        'form': form
    })


def index(request):
    return render(request, 'discord_embed/index.html')


@login_required
def profile(request):
    imgs = Uploaded_image.objects.all()
    files = Uploaded_file.objects.all()
    return render(request, 'discord_embed/profile.html', {'imgs': imgs, "files": files})
