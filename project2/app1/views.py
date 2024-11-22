from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Bike(request):
    return HttpResponse("chandu riding the bike 200km")

def chandu(request):
    return HttpResponse("<h1>dancing on the road</h1>")

def run(request):
    return HttpResponse("<h1><marquee>SURESH RAINA 03</marquee></h1>")

def mrf(request):
    return HttpResponse('<i>MRF BAT PRICE 30000</i>')

def image(request):
    return HttpResponse('''
                           <h1><marquee>SURESH RAINA 03</marquee></h1>
                           <h1>MR.IPL</h1>
                           <img src="https://cdn.pixabay.com/photo/2018/07/31/21/58/lion-3576031_640.jpg" alt="dancing on the road" width="500" height="500">
                        ''')
