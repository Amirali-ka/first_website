from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
def testt (request):
    return JsonResponse ({'key':'value'})
def home_func (request):
    return HttpResponse('this is home')
def about_func (request):
    return HttpResponse('this is about')
def conect_func (request):
    return HttpResponse('this is conect') 