from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Life(request):
    return HttpResponse("Full of Surprises in Chandu Life")

def Love(request):
    return HttpResponse("Full of Love")