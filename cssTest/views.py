from django.shortcuts import render

# Create your views here.
def init(request):
    return render(request,'cssTest/index.html')

def sub(request):
    return render(request,'cssTest/sub.html')
