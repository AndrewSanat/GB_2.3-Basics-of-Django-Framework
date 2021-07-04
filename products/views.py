from django.shortcuts import render
from datetime import datetime
import json

# Create your views here.
# Контроллеры:

def index(request):
    context = {
        'title': 'GeekShop - Главная',
        'navigationText': 'GeekShop',
        'mainTitleText': 'GeekShop Store',
        'mainText': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! \
                    Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
    }
    return render(request, 'products/index.html', context)

def products(request):
    with open('products/fixtures/goods.json', 'r', encoding='utf-8') as file:
        goods = json.load(file)

    context = {
        'title': 'GeekShop - Каталог',
        'navigationText': 'GeekShop',
        'products': goods,
        'copyrightText': f'Copyright GeekShop',
        'currentDate': datetime.now(),
    }
    return render(request, 'products/products.html', context)
