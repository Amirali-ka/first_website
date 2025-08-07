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
    t=get_list_or_404(post,published_date__lte=timezone.now(),status=1)
    n_id,p_id=0,0
    tt=[]
    for i in t :
        tt.append(i.id)
    t=tt.index(pid)
    if pid==max(tt):
        n_id=pid
    elif pid!=max(tt):
        n_id=tt[t+1]
    if pid==min(tt):
        p_id=pid
    elif pid!=min(tt):
        p_id=tt[t-1]
    prev=get_object_or_404(post,pk=p_id,published_date__lte=timezone.now(),status=1)
    next=get_object_or_404(post,pk=n_id,published_date__lte=timezone.now(),status=1)
    return render(request,'blog/blog-single.html',{'postt':postt,'next':next,'prev':prev})

