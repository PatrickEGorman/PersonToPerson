from django.contrib import admin
from django.urls import path

from apps.PostingOrganizer.views import generate_template

urlpatterns = [
    path('category/<str:category>/', generate_template),
]
