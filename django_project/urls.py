"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin#Initiates importation of all admin modules in each application
from django.urls import path, include#Takes a full python import path to another URLconf module that should be “included” in this place
from django.contrib.auth import views as auth_views#To freely remap your login view within your URLconf without having to update the setting.
from . import views#To refer to the current directory from which the file you are viewing is located.

urlpatterns = [
    path('admin/', admin.site.urls),
  path('', views.index),
  path('accounts/', include('django.contrib.auth.urls'))
]

