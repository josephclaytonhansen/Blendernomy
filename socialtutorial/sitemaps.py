from django.contrib import sitemaps
from django.urls import reverse
from .views import Article

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'http'

    def items(self):
        return ['dashboard', 'contact', 'articles']

    def location(self, item):
        return reverse(item)
    
class ArticleSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = 'http'
    def items(self):
        return Article.objects.filter(published=True)
    def lastmod(self, obj):
        return obj.created_at