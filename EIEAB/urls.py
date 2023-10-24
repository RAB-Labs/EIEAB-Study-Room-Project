"""
URL configuration for EIEAB project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('floor1/', views.floor1_view, name='floor1'),
    path('floor2/', views.floor2_view, name='floor2'),
    path('floor3/', views.floor3_view,  name='floor3'),

    path('room1/', views.room1, name='room1'),
    path('room2/', views.room2, name='room2'),
    path('room3/', views.room3, name='room3'),

]

