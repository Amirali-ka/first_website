from django.shortcuts import render
from blog.models import post
# Create your views here.
from django.http import HttpResponse,JsonResponse
def index_view(request):
    return render(request,'website/index.html')
def about_view(request):
    return render(request,'website/about.html')
def contact_view(request):
    return render(request,'website/contact.html')
def test_view(request):
    posts=post.objects.all()
    contex={'posts':posts}
    return render(request,'website/test.html',contex)