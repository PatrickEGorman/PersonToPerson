from django.http import HttpResponse
from django.template import loader

from apps.PostingOrganizer.util import category_to_display


def generate_template(request, category):
    template = loader.get_template('organizer_template.html')
    display = category_to_display[category]
    return HttpResponse(template.render({
        'category_for_urls': category,
        'category_to_display': display}, request))
