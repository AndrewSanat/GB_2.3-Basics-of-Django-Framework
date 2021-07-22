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

def products(request, category_id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'navigationText': 'GeekShop',
        'copyrightText': f'Copyright GeekShop',
        'currentDate': datetime.now(),
        'categories': ProductCategory.objects.all()
    }
    if category_id:
        context['products'] = Product.objects.filter(category_id=category_id)
    else:
        context['products'] = Product.objects.all()
    return render(request, 'products/products.html', context)
