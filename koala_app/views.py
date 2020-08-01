from django.shortcuts import render

# Create your views here.

def main(requests):
    return render(requests, 'main.html')

def outside(request):
    return render(request, 'outside.html')
