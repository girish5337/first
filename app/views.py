from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def karma(request):
    return HttpResponse('<marquee><h1>it is common</h1</marquee>')
