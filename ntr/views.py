from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def simhadri(request):
    return HttpResponse('<h1>simhadri is the best movie in ntr carrier</h1>')

def temper(request):
    return HttpResponse('<h1><marquee>Temper is the best comeback movie in ntr carrier</marquee></h1>')