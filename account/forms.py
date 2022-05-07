from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django import forms
from ads.models import AdsBookmark, Auto


class UserUpdateInfoForm(ModelForm): #форма редактирования данных пользователя

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
            }),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={
                'class': 'form-control'})
        }


class UserRegistrationForm(ModelForm): #форма регистрации пользователя
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control'
            })
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class LoginForm(forms.Form): #форма авторизации пользователя
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RemoveFromBookmark(ModelForm): #форма удаления избранного
    class Meta:
        model = AdsBookmark
        fields = ['user', 'ad']