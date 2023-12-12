from django.contrib.auth import (login, logout,
                                 authenticate,)
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import (UserRegistrationForm, LoginForm,
                    UserUpdateForm, NewPasswordChangeForm)
from django.contrib.auth.decorators import login_required
from .models import UserModel
from .habr_rss import HabrReader
import asyncio


# Create your views here.
def home(request):
    reader = HabrReader()
    news = asyncio.run(reader.main())
    return render(request, 'home.html', {'news': news[:10]})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserRegistrationForm()
    return render(
        request,
        'register.html',
        {'form': form},
    )


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print(email)
            password = form.cleaned_data['password']
            print(password)
            user = UserModel.objects.get(email=email)
            print(user)
            if user is not None:
                login(
                    request,
                    user,
                )
                return redirect('success')
    else:
        form = LoginForm()
    return render(
        request,
        'login.html',
        {'form': form},
    )


@login_required
def user_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(
        request,
        'update.html',
        {'form': form},
    )


@login_required
def change_password(request):
    if request.method == 'POST':
        form = NewPasswordChangeForm(request.user, data=request.POST)

        if form.is_valid():
            user = request.user
            new_password = form.cleaned_data['new_password1']

            user.password = make_password(new_password)
            user.save()

            # Аутентифицировать пользователя заново с новым паролем
            updated_user = authenticate(request, email=user.email, password=new_password)
            if updated_user:
                login(request, updated_user)
            return redirect('success')

    else:
        form = NewPasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def success(request):
    return render(request, 'success.html')
