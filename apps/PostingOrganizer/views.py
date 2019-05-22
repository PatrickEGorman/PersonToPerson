from PersonToPerson.util import render
from apps.PostingOrganizer.models import Category
import httplib2


def item_category(request, category_url):
    category = Category.objects.get(category_url_name=category_url)
    url = "https://charlottesville.craigslist.org/d/" + category.craigslist_url_adder
    http = httplib2.Http()
    response, content = http.request(url, 'GET')
    craigslist_html = content
    return render(request, 'organizer_template.html', {'category': category, 'craigslist_html': craigslist_html})


def view_all(request):
    return render(request, 'organizer_template.html', {'category': 'view_all'})
