from django.http import HttpResponse
from django.template import loader

from apps.PostingOrganizer.models import Category


def render(request, template, args):
    template = loader.get_template(template)
    args['categories'] = Category.objects.all()
    return HttpResponse(template.render(args, request))
