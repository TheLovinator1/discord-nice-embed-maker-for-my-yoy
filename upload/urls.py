from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/image/', views.upload_images, name="upload_images"),
    path('upload/files/', views.upload_files, name="upload_files"),
    path('accounts/profile/', views.profile, name='account_profile'),
]
