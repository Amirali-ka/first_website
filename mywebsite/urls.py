
from django.urls import path
from mywebsite.views import *

urlpatterns = [
    path('', home_func),
    path('about/',about_func),
    path('conect/',conect_func)
]