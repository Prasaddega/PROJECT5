from ntr.views import *

from django.urls import path

app_name='something'

urlpatterns=[
    path('simhadri/',simhadri,name='simhadri'),
    path('temper/',temper,name='temper'),
]