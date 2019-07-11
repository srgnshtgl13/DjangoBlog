"""poster URL Configuration

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
from django.urls import path, re_path, include
from home.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', HomePageView.as_view(), name='home'),
    re_path(r'^about/$', AboutPageView.as_view(), name='about'),
    re_path(r'^post/', include('post.urls')),
    re_path(r'^profile/', include('userprofile.urls')),
    path('accounts/', include('registration.urls', namespace="accounts")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


