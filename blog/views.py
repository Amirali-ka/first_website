from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from blog.models import post
# Create your views here.
def blog_view(request):
    posts=post.objects.filter(published_date__lte=timezone.now(),status=1)
    return render(request,'blog/blog-home.html',{'posts':posts})
def single_view(request,pid):
    posts=get_object_or_404(post,pk=pid,published_date__lte=timezone.now(),status=1)
    posts.counted_views+=1
    posts.save()
    return render(request,'blog/blog-single.html',{'posts':posts})
