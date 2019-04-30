from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def get_facebook_access_token(request):
    response = HttpResponse('')
    return response.cookies.get('facebook_access_token')
