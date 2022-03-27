# dwitter/urls.py

from django.urls import path, include, re_path
from .views import (dashboard, test, old_admin, page_not_found, article_random,
ArticleView, ArticleList, TagView, ContactView, ContactSuccessView, ProductView,
KeyValidatorView, PurchaseView, SuperTagView)
from .models import Article
from django.conf.urls import handler404
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap # new
from django.contrib.sitemaps.views import sitemap # new

app_name = "socialtutorial"

info_dict = {
    'queryset': Article.objects.all(),
}

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("index/", dashboard, name="dashboard"),
    path("test", test, name="test"),
    path("articles", ArticleList.as_view(), name="articles"),
    path("random", article_random, name="article_random"),
    path('<slug:slug>/', ArticleView.as_view(), name='article'),
    path('tag/<slug:slug>', TagView.as_view(), name='tag'),
    path('child-tag/<slug:slug>', SuperTagView.as_view(), name='supertag'),
    path('product/<slug:slug>', ProductView.as_view(), name='product'),
    path('g/<slug:slug>', PurchaseView, name='purchaseview'),
    path("admin", old_admin, name = "old_admin"),
    path("wp-admin", old_admin, name = "old_admin"),
    path("wp-login", old_admin, name = "old_admin"),
    path("dashboard", old_admin, name = "old_admin"),
    path("gateway", old_admin, name = "old_admin"),
    path('contact', ContactView.as_view(), name="contact"),
    path('contact_success', ContactSuccessView.as_view(), name="success"),
    path('key_validation', KeyValidatorView, name="key_validation"),
    path('sitemap.xml', sitemap, # new
        {'sitemaps': {'socialtutorial': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += [
    path('captcha/', include('captcha.urls'))
    ]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = page_not_found