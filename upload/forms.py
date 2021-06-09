from django import forms
from .models import *
  
class UploadForm(forms.ModelForm):
  
    class Meta:
        model = FileUpload
        fields = '__all__'