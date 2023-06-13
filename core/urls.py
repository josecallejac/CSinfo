"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include

from .views import HomeView
from hltv import views

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('csinfo/', include('csinfo.urls', namespace="csinfo")),
    path('accounts/', include('allauth.urls')),
    path('users/', include('accounts.urls', namespace='users')),

    path("__reload__/", include("django_browser_reload.urls")),
    path('', HomeView.as_view(), name="home"),
    path('hltv/', include('hltv.urls', namespace="hltv")),

    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title='Api CSinfo Documentation'))
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_URL)
