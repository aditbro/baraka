"""baraka URL Configuration

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
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='mainpage'),
    path('about/', views.about_us, name='about us'),
    path('contact/', views.contact, name='contact'),
    path('lowongan_kerja/jabar', views.loker_jabar),
    path('lowongan_kerja/jateng', views.loker_jateng),
    path('lowongan_kerja/jatim', views.loker_jatim),
    path('lowongan_kerja/jakarta', views.loker_jakarta),
]
