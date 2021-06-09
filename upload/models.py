from django.db import models

# Create your models here.
class FileUpload(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    Main_File = models.FileField(upload_to='%m%d/',null=True, blank=True)