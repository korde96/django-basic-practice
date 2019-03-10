from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import NumForm

def index(request):
    if(request.method == 'POST'):
        form = NumForm(request.POST)

        if form.is_valid():
            r = form.cleaned_data['fnum']
            nums = [int(x) for x in r.strip().split()]
            oddEvenSort(nums, len(nums))
            st = ""
            for x in nums:
                st = st + str(x) + " "
            return render(request,'oddeven/base.html',{'form':form, 'st':st})
    else:
        form = NumForm()
        return render(request,'oddeven/base.html',{'form':form})

def oddEvenSort(arr, n):
    # Initially array is unsorted
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0

        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0

    return
