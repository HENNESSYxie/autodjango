from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm, UserRegistrationForm, UserUpdateInfoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from ads.models import AdsBookmark, Auto


def register(request): #функция регистрация пользователя
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST) #используем форму которую создавали в forms.py для регистрации
        if user_form.is_valid(): #проверка валидности данных
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save() #сохраняем объект пользователя
            return render(request, 'account/register_done.html', {'new_user': new_user}) #перенаправляем на страницу с успешной регистрацией
    else:
        user_form = UserRegistrationForm() #если форма не валидная, то возвращаем эту же форму для повторного ввода данных
    return render(request, 'account/register.html', {'user_form': user_form})


def user_login(request): #авторизация пользователя
    if request.method == 'POST':
        form = LoginForm(request.POST) #используем форму авторизации из forms.py
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return dashboard(request)
                else:
                    return render(request, 'account/login.html', {'form': form, 'message': 'Аккаунт деактивирован'})
            else:
                return render(request, 'account/login.html', {'form': form, 'message': 'Неверный логин или пароль'})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required #декоратор login_required устанавливает условие, что пользователь должен быть авторизован
def dashboard(request):
    bookmarks_objects = AdsBookmark.objects.filter(user=request.user.id)
    ads = list()
    for bookmark in bookmarks_objects:
        ads.append(Auto.objects.get(id=bookmark.ad))
    data = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'favorites': ads
    }
    return render(request, 'account/dashboard.html', data)


@login_required
def logout(request): #Выход из аккаунта
    django_logout(request)
    return render(request, 'account/logged_out.html')


@login_required
def edit_profile(request): #редактировать аккаунт
    if request.method == 'POST':
        form = UserUpdateInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserUpdateInfoForm(instance=request.user, initial={'first_name': request.user.first_name,
                                                                  'email': request.user.email})
    return render(request, 'account/edit_profile.html', {'form': form})


@login_required
def remove_from_favorites(request, pk): #удалить из избранного
    ad = AdsBookmark.objects.get(user=request.user.id, ad=pk)
    ad.delete()
    return redirect(request.META['HTTP_REFERER'])

