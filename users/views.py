from django.contrib.auth import (authenticate,
                                 login, update_session_auth_hash)
from django.shortcuts import render, redirect
from .forms import (UserRegistrationForm, LoginForm,
                    UserUpdateForm, CustomPasswordChangeForm)
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')


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
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
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
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(
        request,
        'change_password.html',
        {'form': form},
    )
