from django.http import HttpResponse
from django.template import loader

from apps.PostingOrganizer.models import Category


def home(request):
    template = loader.get_template('home.html')
    categories = Category.objects.all()
    return HttpResponse(template.render({'categories': categories}, request))
