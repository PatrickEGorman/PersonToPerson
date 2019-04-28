from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from apps.MarketPlaces.Api.Craigslist.util import urlBuilder


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))
