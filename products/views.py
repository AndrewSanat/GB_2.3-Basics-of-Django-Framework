from django.shortcuts import render
from datetime import datetime
from products.models import Product, ProductCategory

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

    context = {
        'title': 'GeekShop - Каталог',
        'navigationText': 'GeekShop',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'copyrightText': f'Copyright GeekShop',
        'currentDate': datetime.now(),
    }
    return render(request, 'products/products.html', context)
