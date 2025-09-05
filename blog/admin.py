from django.contrib import admin
from blog.models import post,category
from mywebsite.models import Contact,newsletter
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class postadmin(SummernoteModelAdmin):
    date_hierarchy='published_date'
    empty_value_display='-empty-'
    list_display=('title','counted_views','author','status','published_date','created_date')
    list_filter=('status','author')
    search_fields=['title','content']
    summernote_fields = ('content',)

admin.site.register(post,postadmin)
admin.site.register(category)
admin.site.register(Contact)
admin.site.register(newsletter)