from django.shortcuts import render

def login(request):
    context = {
        'title': 'Авторизация',
    }
    return render(request, 'users/login.html', context=context)

def registration(request):
    context = {
        'title': 'Регистрация',
    }
    return render(request, 'users/registration.html', context=context)

def profile(request):
    context = {
        'title': 'Кабинет',
    }
    return render(request, 'users/profile.html', context=context)

def logout(request):
    context = {
        'title': '',
    }
    return render(request, '', context=context)