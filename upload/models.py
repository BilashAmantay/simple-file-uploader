from django.db import models

# Create your models here.
class ImageUpload(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    Main_Img = models.ImageField(upload_to='images/%m%d/')