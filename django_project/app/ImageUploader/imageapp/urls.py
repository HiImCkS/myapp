from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('upload/', views.upload_image, name='upload_image'),
    path('gallery/', views.image_gallery, name='image_gallery'),
   
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
