from django.contrib import messages
from multiprocessing import context
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Facilidades, Hotel, HotelReserva
from django.db.models import Q

def home(request):
    facilidades = Facilidades.objects.all()
    hotels = Hotel.objects.all()
    
    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    facil = request.GET.getlist('facil')
    print(facil)
    if sort_by:
        if sort_by == 'ASC':
            hotels = hotels.order_by('hotel_preco')
        elif sort_by == 'DSC':
            hotels = hotels.order_by('-hotel_preco')
    if search:
        hotels = hotels.filter(
            Q(hotel_nome__icontains=search)|
            Q(descricao__icontains=search)
        )
    
    if len(facil):
        hotels = hotels.filter(facilidades__facilidade_nome__in=facil).distinct()
        
    context = {
        'facilidades':facilidades,
        'hotels':hotels,
        'sort_by':sort_by,
        'search':search
    }
    return render(request, 'home/home.html', context)

def verifica_reserva(inicio, fim, uid, qtd_quartos):
    qs = HotelReserva.objects.filter(
        data_inicio__lte=inicio,
        data_fim__gte=fim,
        hotel__uid = uid,
        
    )
    if len(qs) >= qtd_quartos:
        return False
    return True

def hotel_detail(request, uid):
    hotel = Hotel.objects.get(uid=uid)
    
    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        hotel = Hotel.objects.get(uid=uid)
        if not verifica_reserva(checkin, checkout, uid, hotel.qtd_quartos):
            messages.warning(request, 'Hotel já reservado para essas datas')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        HotelReserva.objects.create(
            hotel=hotel,
            user=request.user,
            data_inicio = checkin,
            data_fim=checkout,
            tipo_de_reserva='Pre Pagamento'
        )
        messages.success(request, 'Sua reserva foi salva!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        'hotel':hotel
    }
    return render(request, 'home/hotel_detail.html', context)


    