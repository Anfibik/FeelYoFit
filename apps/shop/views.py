from django.shortcuts import render


def index(request):
    gammaks = {
        'Standard': "Йога-гаммак \"Стандарт\"",
        'Comfort': "Йога-гаммак \"Комфорт\"",
        'Lux': "Йога-гаммак \"Люкс\""
    }
    return render(request, 'shop/index.html', context={'gammaks': gammaks})
