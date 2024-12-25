from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def main_page(request):
    return render(request, 'fourth_task/main_page.html')


def aqara(request):
    title = 'Aqara'
    categories = ['Датчики', 'Освещение', 'Управление']
    context = {
        'title': title,
        'categories': categories
    }
    return render(request, 'fourth_task/first_page.html', context)


def moes(request):
    title = 'MOES'
    categories = ['Переключатели', 'Термостаты', 'Розетки']
    context = {
        'title': title,
        'categories': categories
    }
    return render(request, 'fourth_task/second_page.html', context)
