from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')


def aqara(request):
    title = 'Aqara'
    sensors = 'Датчики'
    lightning = 'Освещение'
    hubs = 'Управление'
    context = {
        'title': title,
        'text_1': sensors,
        'text_2': lightning,
        'text_3': hubs,
    }
    return render(request, 'first_page.html', context)


def moes(request):
    title = 'MOES'
    switch = 'Переключатели'
    thermostat = 'Термостаты'
    socket = 'Розетки'
    context = {
        'title': title,
        'text_1': switch,
        'text_2': thermostat,
        'text_3': socket,
    }
    return render(request, 'second_page.html', context)
