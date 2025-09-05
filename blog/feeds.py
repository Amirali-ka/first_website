from django.contrib.syndication.views import Feed
from blog.models import post


class LatestEntriesFeed(Feed):
    title = "blog newst post"
    link = "/rss/feed"
    description = "best blog"

    def items(self):
        return post.objects.filter(status=True)
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.content