from django.http import HttpResponse
from django.template import loader

from apps.MarketPlaces.models import Location
from apps.PostingOrganizer.models import Category


def home(request):
    template = loader.get_template('home.html')
    categories = Category.objects.all()
    return HttpResponse(template.render({'categories': categories}, request))


def set_location(request):
    response = HttpResponse('')
    response.set_cookie('location_lat', request.POST.get('lat', None))
    response.set_cookie('location_long', request.POST.get('long', None))
    return HttpResponse('')
