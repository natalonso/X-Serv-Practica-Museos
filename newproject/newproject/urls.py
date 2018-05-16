"""newproject URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.auth.views import login
from django.views.static import serve
from newproject import settings

urlpatterns = [

    url(r'^logout$', logout),
    url(r'^login', login),
    url(r'^$','museos.views.principal'),
    url(r'^(\d+)$','museos.views.principal_anotada'),
    url(r'^museos$','museos.views.museos'),
    url(r'^museo/(\d+)$','museos.views.museo_id'),
    url(r'^(\w+)/xml$','museos.views.usuario_xml'),
    url(r'^about$','museos.views.about'),
    url(r'^(\w+)$','museos.views.usuario'),
    url(r'^(\w+)/(\d+)$','museos.views.usuario_anotada'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'(style.css/)$', serve, {'document_root': "templates/museos"}),
    url(r'(foto.png/)$', serve, {'document_root': "templates/museos"})


]
