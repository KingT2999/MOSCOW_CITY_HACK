from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Volunteer
from .forms import *

# Create your views here.
def register_page(request):
    context = {}

    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        volunteer_form = VolunteerForm(request.POST)

        if user_form.is_valid() and volunteer_form.is_valid():
            user = user_form.save()

            Volunteer.create(user=user, birth_date=request.POST.get('birth_date'))

        return redirect('accounts:register_page')
    else:
        context['user_form'] = CreateUserForm()
        context['volunteer_form'] = VolunteerForm()


    return render(request, 'accounts/register_page.html', context)

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            return redirect('accounts:register_page')
        else:
            messages.error(request, 'Имя пользователья и/или пароль введены не правильно')

    return render(request, 'accounts/login_page.html')

def logout_page(request):
    logout(request)

    return redirect('accounts:login_page')