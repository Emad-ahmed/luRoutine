from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# def login(requests):
#     return render(requests, 'login.html', {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('core:home'))
        else:
            return render(request, 'login.html', context={
                'error': 1
            })
    else:
        return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:user_login'))
