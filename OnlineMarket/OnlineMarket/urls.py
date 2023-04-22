"""
URL configuration for OnlineMarket project.

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
from Pedidos import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login),
    path('admin/', admin.site.urls),
    path('search/', views.buscar_productos),
    path('ProductDetail/', views.buscar),
    path('contact/', views.contacto),
    path('register/', views.register),
    path('home/', views.home),
    path('forum/', views.foro),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

