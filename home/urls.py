from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('hotel_detail/<uid>/', views.hotel_detail, name='hotel_detail'),
    path('verifica_reserva/', views.verifica_reserva, name='verifica_reserva')
]