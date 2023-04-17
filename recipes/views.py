from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    ...
    # return HTTP response
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Matheus Henrique',
    })


def recipe(request, id):
    ...
    # return HTTP response
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Matheus Henrique',
    })
