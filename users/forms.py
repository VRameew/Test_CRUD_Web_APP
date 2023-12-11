from django import forms
from django.contrib.auth.forms import SetPasswordForm, authenticate
from .models import UserModel
import re


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('email', 'user_name',
                  'password',
                  'first_name', 'last_name')

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            if password == '':
                raise forms.ValidationError('Укажите пароль')
            return cleaned_data

        def save(self, commit=True):
            user = super().save(commit=False)
            user.password = self.cleaned_data['password']
            if commit:
                user.save()
            return user


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email'
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            user = authenticate(
                username=email,
                password=password,
            )
            print(user)
            if not user:
                #print(cleaned_data)
                raise forms.ValidationError('Не верный логин или пароль')
        return cleaned_data


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'user_name', 'first_name', 'last_name']


class NewPasswordChangeForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label='Confirm new password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')

        # Проверка на использование заглавной буквы и цифры
        if not re.search(r'^(?=.*[A-Z])(?=.*\d)', password):
            raise forms.ValidationError("Пароль должен содержать как минимум одну заглавную букву и одну цифру.")

        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('new_password1')
        password2 = cleaned_data.get('new_password2')

        # Проверка на идентичность паролей
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")

        return cleaned_data
