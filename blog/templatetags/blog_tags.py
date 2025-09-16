from django import template
from django.utils import timezone
from blog.models import post,category,comment
register=template.Library()
@register.simple_tag(name='func')
def func ():
     posts=post.objects.filter(status=1)
     return posts
@register.simple_tag(name='counted_view')
def counted_view (pid):
     return comment.objects.filter(post=pid,approach=True).count()
@register.filter()
def funcc (value):
     return value[:100]
@register.inclusion_tag('populartemp.html')
def pop_date():
     posts = post.objects.filter(status=1).order_by('-published_date')[:1]
     return {'posts':posts}
@register.inclusion_tag('blog/popular_post.html')
def lastestpost(x=1):
     posts=post.objects.filter(status=1).order_by('published_date')[:x]
     return {'posttt':posts}
@register.inclusion_tag('blog/post_category.html')
def postcategory():
     posts=post.objects.filter(status=1)
     categories=category.objects.all()
     cat_dict={}
     for name in categories:
          cat_dict[name]=posts.filter(category=name).count()
     return {'categories':cat_dict}
@register.inclusion_tag('website/lastest_post.html')
def lastestposts(x=6):
     posts = post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-published_date')
     posts = list(posts)          
     posts.reverse()              
     posts = posts[:x] 
     return {'posts':posts}