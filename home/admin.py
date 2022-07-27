from django.contrib import admin
from .models import Hotel, HotelImagem, Facilidades, HotelReserva
# Register your models here.

admin.site.register(Facilidades)
admin.site.register(Hotel)
admin.site.register(HotelImagem)
admin.site.register(HotelReserva)