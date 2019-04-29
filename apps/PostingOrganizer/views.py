from django.http import HttpResponse
from django.template import loader


def generate_template(request, category):
    template = loader.get_template('organizer_template.html')
    return HttpResponse(template.render({
        'category_for_urls': category}, request))
