
location = "charlottesville"

category_url_extensions = {"musical-instruments": "msa"}


def urlBuilder(category):
    if category not in category_url_extensions:
        raise Exception("%s is not a supported category" % category)
    search_string = category_url_extensions[category]
    return "https://%s.craigslist.org/d/%s/search/%s" % (location, category, search_string)
