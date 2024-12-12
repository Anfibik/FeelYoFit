from django.shortcuts import render

from django.conf import settings


def index(request):
    for directory in settings.TEMPLATES[0]['DIRS']:
        print(f"Папка для шаблонов: {directory}")
    return render(request, 'shop/index.html')
