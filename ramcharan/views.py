from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def magadheera(request):
    return HttpResponse('<h1>magadheera movie is best movie in ramcharan carrier</h1>')

def rangasthalam(request):
    return HttpResponse('<h1>rangasthalam movie is best nativity movie in ramcharan carrier</h1>')