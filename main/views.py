from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'The main page of shop Home'
    }
    
    return render(request, 'main\index.html', context=context)

def about(request):
    return HttpResponse ('About page')
