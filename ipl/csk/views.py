from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msdhoni(request):
    return HttpResponse('<h1>MSD is a great captain<h1>')
def captain(request):
    return HttpResponse('<h1>Ruthraj Gaikwad was new captain for CSK<h1>')