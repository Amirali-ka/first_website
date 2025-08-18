from django.shortcuts import render,get_object_or_404
from blog.models import post
# Create your views here.
def index_view(request):
    return render(request,'website/index.html')
def about_view(request):
    return render(request,'website/about.html')
def contact_view(request):
    return render(request,'website/contact.html')
def test_view(request):
    return render(request,'website/test.html')