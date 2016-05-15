"""task3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', 'site3.views.mainpage'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^materials/material1.html$','site3.views.material1'),
    url(r'^materials/material2.html$','site3.views.material2'),
    url(r'^materials/material3.html$','site3.views.material3'),
    url(r'^materials/material4.html$','site3.views.material4'),
    url(r'^materials/material5.html$','site3.views.material5'),
    url(r'^materials','site3.views.materials'),
    url(r'^tasks','site3.views.tasks', name='tasks'),
    url(r'^tests','site3.views.tests'),
    url(r'^links','site3.views.links'),
    url(r'^favourites','site3.views.favourites'),
    url(r'^addtofavourites/(?P<pagename>\w+)$','site3.views.create_favourite', name='addtofavourites'),
    url(r'^deletefromfavourites/(?P<pagename>\w+)$','site3.views.delete_favourite', name='deletefromfavourites')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)