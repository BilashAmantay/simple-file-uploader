from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def image_upload_view(request):

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ImageUploadForm(request.POST)
            return render(request, 'upload/index.html', {'form': form})
    else:
        form = ImageUploadForm()
    return render(request, 'upload/index.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
