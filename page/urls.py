from django.contrib import admin
from django.urls import path, include
from .views import HomePage, AboutPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about', AboutPage.as_view(), name='about'),
]
