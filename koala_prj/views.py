from django.shortcuts import render

# Create your views here.
def outside(request):
    return render(request, 'outside.html')