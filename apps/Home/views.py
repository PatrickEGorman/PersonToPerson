from PersonToPerson.util import render


def home(request):
    return render(request, 'home.html', {})


def privacy_policy(request):
    return render(request, 'privacy.html', {})
