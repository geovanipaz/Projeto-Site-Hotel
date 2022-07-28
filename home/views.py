from multiprocessing import context
from django.shortcuts import render
from .models import Facilidades, Hotel


def home(request):
    facilidades = Facilidades.objects.all()
    hotels = Hotel.objects.all()
    context = {
        'facilidades':facilidades,
        'hotels':hotels,
    }
    return render(request, 'home/home.html', context)
