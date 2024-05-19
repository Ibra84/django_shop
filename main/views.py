from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная',
        'content': 'Магазин мебели HOME',
    }
    
    return render(request, 'main\index.html', context=context)

def about(request):
    context = {
        'title': 'About us',
        'content': 'About us',
        'text_on_page': 'Text about why this shop is the best and our goods are best im the world'
    }
    return render(request, 'main/about.html', context=context)
 
def contacts(request):
    context = {
        'title': 'Contacts',
        'content': 
            'Phone: +992 93 594 54-65',
            
        'text_on_page': 'You can contact us when you need some help'
    }
    return render(request, 'main/contacts.html', context=context)

def delivery(request):
    context = {
        'title': 'Delivery',
        'content': 'Delivery',
        'text_on_page': 'You can make an order here and pay for it'
    }
    return render(request, 'main/delivery.html', context=context)