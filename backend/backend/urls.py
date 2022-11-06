"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from backendApp import views
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('get_users/', views.get_users),
    path('get_rooms/', views.get_rooms),
    path('get_messages/<int:room_id>', views.get_messages),
    path('get_cookie/<int:user_id>', views.get_cookie),
    path('auth/', views.auth),
    path('send_message/', views.send_message),
]
