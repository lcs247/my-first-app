"""Infochannel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from redflags.Apps.Videos import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^formulario/', views.vista_formulario, name='formulario'),
    url(r'^formulario/', views.formulario.as_view(), name='formulario'),
    url(r'^lista_ubicaciones/', views.vista_listado_mapa, name='vista_listado_mapa'),
    url(r'^mapa/', views.vista_mapa, name='mapa'),
    url(r'^$', views.inicio, name='inicio')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


