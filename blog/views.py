from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage
from django.utils import timezone
from blog.models import post
# Create your views here.
def blog_view(request):
    posts=post.objects.filter(published_date__lte=timezone.now(),status=1)
    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except EmptyPage :
        posts=posts.get_page(1)
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
def blog_category(request,cat_str):
    posts=post.objects.filter(published_date__lte=timezone.now(),status=1,category__name=cat_str)
    return render(request,'blog/blog-home.html',{'posts':posts})
def blog_author(request,author_username):
    if author_username :
        posts=post.objects.filter(published_date__lte=timezone.now(),status=1,author__username=author_username)
    return render(request,'blog/blog-home.html',{'posts':posts})
def blog_search(request):
    posts=post.objects.filter(status=1)
    if request.method=='GET':
        posts=post.objects.filter(content__contains=request.GET.get('s'))
    
    return render(request,'blog/blog-home.html',{'posts':posts})