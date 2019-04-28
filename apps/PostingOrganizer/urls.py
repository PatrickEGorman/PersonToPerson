from django.contrib import admin
from django.urls import path

from apps.Home.views import home

urlpatterns = [
    path('musical-instruments/', home),
]
