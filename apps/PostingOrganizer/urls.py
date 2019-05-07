from django.contrib import admin
from django.urls import path

from apps.PostingOrganizer.views import item_category, view_all

urlpatterns = [
    path('category/<str:category_url>/', item_category),
    path('view_all', view_all),
]
