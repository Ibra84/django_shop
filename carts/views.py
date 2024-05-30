from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from carts.models import Cart
from goods.models import Products

def cart_add(request,product_slug):
    product = Products.objects.get(slug=product_slug)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity +=1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
                
    return redirect(request.META['HTTP_REFERER'])                



def cart_change(request, product_slug):
    if request.method == 'POST':
        new_quantity_str = request.POST.get('quantity')
        if new_quantity_str is not None:
            new_quantity = int(new_quantity_str)
            if not new_quantity == 0:
                product = get_object_or_404(Products, slug=product_slug)
                cart = get_object_or_404(Cart, user=request.user, product=product)
                cart.quantity = new_quantity
                cart.save()    
        
    return redirect(request.META['HTTP_REFERER'])



def cart_remove(request,cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
    
    
