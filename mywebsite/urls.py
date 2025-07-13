
from django.urls import path
from mywebsite.views import *

urlpatterns = [
    path('', index_view),
    path('main/', main_menu),
    path('about/',about_func),
    path('conect/',conect_func)
]