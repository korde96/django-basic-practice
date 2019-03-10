from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import UploadFileForm

def index(request):
    st = ""
    if request.method == 'POST':
        print("POST")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['file'].name)
    else:
        form = UploadFileForm()
    return render(request, 'plagiarism/base.html', {'form': form,'st':st})
