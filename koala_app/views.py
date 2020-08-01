from django.shortcuts import render

# Create your views here.

def outside(request):
    return render(request, 'outside.html')

def inside(request):
    return render(request, 'home(1).html')

def outside_detail(request):
    return render(request, '밖(5).html')

def inside_detail(request):
    return render(request, 'inside_detail.html')

def home(request):
    return render(request, 'mainpage.html')

