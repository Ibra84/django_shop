from django.shortcuts import render
from goods.models import Products

def catalog(request):
    
    goods = Products.objects.all()
    
    context = {
        'title': 'Catalog',
        'goods': goods,
         
}
    return render(request, 'goods/catalog.html', context=context)

def product(request):
    context = {
        
    }
    return render(request, 'goods/product.html', context=context)