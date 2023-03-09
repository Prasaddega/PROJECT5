from ramcharan.views import *

from django.urls import path

app_name='nothing'

urlpatterns=[
    path('magadheera/',magadheera,name='magadheera'),
    path('rangasthalam/',rangasthalam,name='rangasthalam'),
]