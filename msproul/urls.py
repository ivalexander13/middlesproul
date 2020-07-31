"""msproul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import read_pki
from landing import views as landing_views
from django.conf import settings
from django.conf.urls.static import static 

try:
   from secrets_dev import pki_val
except ImportError:
    raise Exception("A secrets_XXX.py file is required to run this project")

urlpatterns = [
    path('/admin/', admin.site.urls), # fixme with admin/
    path(pki_val, read_pki.read_file),
    path('', landing_views.coming_soon)
]
