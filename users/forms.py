from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserModel


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('email', 'user_name', 'password', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        if UserModel.objects.filter(user_name=user_name).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        return user_name

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
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


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'user_name', 'first_name', 'last_name']


class CustomPasswordChangeForm(PasswordChangeForm):
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']