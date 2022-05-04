from django.shortcuts import render


def about(request):
    return render(request, 'ads/about.html')


def contacts(request):
    return render(request, 'ads/contacts.html')
