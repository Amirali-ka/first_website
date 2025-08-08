from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.utils import timezone
from blog.models import post
# Create your views here.
def blog_view(request):
    posts=post.objects.filter(published_date__lte=timezone.now(),status=1)
    return render(request,'blog/blog-home.html',{'posts':posts})
def single_view(request,pid):
    postt=get_object_or_404(post,pk=pid,published_date__lte=timezone.now(),status=1)
    postt.counted_views+=1
    postt.save()
    try:
        prev_post = post.objects.filter(published_date__lte=timezone.now(),status=1,pk__lt=pid).order_by('-pk').first()
    except post.DoesNotExist:
        prev_post = None

    try:
        next_post = post.objects.filter(published_date__lte=timezone.now(),status=1,pk__gt=pid).order_by('pk').first()
    except post.DoesNotExist:
        next_post = None
    return render(request,'blog/blog-single.html',{'postt':postt,'next':next_post,'prev':prev_post})

