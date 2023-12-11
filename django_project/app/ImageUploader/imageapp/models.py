# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UploadedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    image_type = models.CharField(max_length=20, choices=(('Portrait', 'Portrait'), ('Landscape', 'Landscape')))
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
