"""try_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps import views as sitemap_views

from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView, SearchView, AuthorView,
)
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from config.views import LinkView
from comment.views import CommentView
from .custom_site import custom_site


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<category_id>/', CategoryView.as_view(), name='category-list'),
    path('tag/<tag_id>/', TagView.as_view(), name='tag-list'),
    path('post/<post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('links/', LinkView.as_view() , name='links'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<owner_id>/', AuthorView.as_view(), name='author'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('rss/', LatestPostFeed(), name='rss'),
    path(r'sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    path('super_admin/', admin.site.urls, name='super-admin'),
    path('admin/', custom_site.urls, name='admin'),
]
