from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    ...
    # return HTTP response
    return render(request, 'recipes/home.html', context={
        'name': 'Matheus Henrique',
    })


def sobre(request):
    ...
    # return HTTP response
    return HttpResponse("sobre")


def contato(request):
    ...
    # return HTTP response
    return HttpResponse("CONTATO")
