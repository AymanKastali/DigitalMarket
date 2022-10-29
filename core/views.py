from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'core/index.html', context)

def browse(request):
    context = {}
    return render(request, 'core/browse.html', context)

def favorites(request):
    context = {}
    return render(request, 'core/favorites.html', context)

def bookmarks(request):
    context = {}
    return render(request, 'core/bookmarks.html', context)

def ads(request):
    context = {}
    return render(request, 'core/ads.html', context)