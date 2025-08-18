from django import template
from blog.models import post
register=template.Library()
@register.simple_tag(name='func')
def func ():
     posts=post.objects.filter(status=1)
     return posts
@register.filter()
def funcc (value):
     return value[:100]
@register.inclusion_tag('populartemp.html')
def pop_date():
     posts=post.objects.filter(status=1).order_by('published_date')[:1]
     return {'posts':posts}
@register.inclusion_tag('blog/popular_post.html')
def lastestpost(x=1):
     posts=post.objects.filter(status=1).order_by('published_date')[:x]
     return {'posttt':posts}