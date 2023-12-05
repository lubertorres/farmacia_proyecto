from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'producto/plantilla_base.html');


def producto(request):
    return render(request,'producto/dashboard.html')

def aboutU(request):
    return render(request, 'producto/aboutUs.html')
