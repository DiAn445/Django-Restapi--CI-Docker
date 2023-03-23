from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    if 'american' in request.POST:
        plus_like(american)
    elif 'manul' in request.POST:
        plus_like(manul)
    elif 'abyss' in request.POST:
        plus_like(abyss)
    elif 'siamese' in request.POST:
        plus_like(siamese)
    elif 'bengal' in request.POST:
        plus_like(bengal)
    elif 'british' in request.POST:
        plus_like(british)

    context = {'Title': 'Cats', 'american': american.likes, 'british': british.likes, 'bengal': bengal.likes,
               'siamese': siamese.likes,
               'manul': manul.likes, 'abyss': abyss.likes}

    return render(request, 'cats/index.html', context=context)


@csrf_protect
def about(request):
    return render(request, 'cats/about.html', {'Title': 'Anya'})


def show_post(request, post_id):
    return HttpResponse(f"card num: {post_id}")