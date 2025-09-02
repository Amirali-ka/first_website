from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns = [
    path('', blog_view ,name='index'),
    path('post-<int:pid>',single_view ,name='single'),
    path('category-<str:cat_str>',blog_category ,name='category'),
    path('author-<str:author_username>',blog_author ,name='author'),
    path('tags-<str:tag_str>',blog_tags ,name='tags'),
    path('search/',blog_search ,name='search'),
]