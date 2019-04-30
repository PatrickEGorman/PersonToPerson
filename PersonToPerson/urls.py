"""PersonToPerson URL Configuration

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
from django.urls import include, path

from apps.Home.views import home, set_location, privacy_policy
from apps.MarketPlaces.views import set_facebook_access_token

urlpatterns = [
    path('', home),
    path('posting_organizer/', include('apps.PostingOrganizer.urls')),
    path('privacy_policy', privacy_policy),
    path('admin/', admin.site.urls),
]
