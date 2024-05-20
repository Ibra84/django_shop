from django.shortcuts import render

def catalog(request):
    context = {
        
    }
    return render(request, 'goods/catalog.html', context=context)

def product(request):
    context = {
        
    }
    return render(request, 'goods/product.html', context=context)