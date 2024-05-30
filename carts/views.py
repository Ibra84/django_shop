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



def cart_change(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id, user=request.user)
    
    if request.method == 'POST':
        action = request.GET.get('action')
        
        if action == 'increase':
            cart.quantity += 1
            cart.save()
        elif action == 'decrease':
            if cart.quantity > 1:
                cart.quantity -= 1
                cart.save()
            else:
                cart.delete()
        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)
        
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))



def cart_remove(request,cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
    
    
