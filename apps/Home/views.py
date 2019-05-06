from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from apps.PostingOrganizer.models import Category


def home(request):
    template = loader.get_template('home.html')
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


def privacy_policy(request):
    template = loader.get_template('privacy.html')
    return HttpResponse(template.render({}, request))
