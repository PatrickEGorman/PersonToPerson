from PersonToPerson.util import render
from apps.PostingOrganizer.models import Category


def item_category(request, category_url):
    category = Category.objects.get(category_url_name=category_url)
    return render(request, 'organizer_template.html', {'category': category})


def view_all(request):
    return render(request, 'organizer_template.html', {'category': 'view_all'})
