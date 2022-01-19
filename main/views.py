from django.shortcuts import render
from . import models
from datetime import date


def index(request):
    services = models.services.objects.all()
    for service in services:
        service.ais = service.photos.all()
    slider = models.slider.objects.all()
    pages = models.pages.objects.all()
    gallery = models.gallery.objects.all()
    first = models.firstBlock.objects.all()[:1].get()
    year = date.today().strftime('%Y')

    context = {'services': services, 'slider': slider, 'pages': pages, 'gallery': gallery, 'year': year,
               'first': first}
    return render(request, 'basic.html', context)

