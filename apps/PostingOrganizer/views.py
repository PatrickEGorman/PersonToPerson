from django.http import HttpResponse
from django.template import loader

from apps.PostingOrganizer.models import Category


def generate_template(request, category_url):
    template = loader.get_template('organizer_template.html')
    category = Category.objects.get(category_url_name=category_url)
    return HttpResponse(template.render({
        'category': category}, request)
    )
