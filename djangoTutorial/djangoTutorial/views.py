from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello world.This is home page")
    return render(request,'index.html')