
from django.urls import path,re_path
from mywebsite.views import *

app_name='website'

urlpatterns = [
    re_path(r'^.*$', coming_view),
    path('', index_view,name='index'),
    path('about/',about_view,name='about'),
    path('contact/',contact_view,name='contact'),
    path('newsletter/',newsletter_view,name='newsletter')
]