from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Auto, AdsBookmark
from .forms import FilterAds
from django.contrib.auth.decorators import login_required

queryset = None


# Create your views here.
def index(request): #рендер главной страницы
    if request.method == 'POST': #Если запрос пост, то мы должны проверить фильтры
        form = FilterAds(request.POST)
        if form.is_valid():
            objects = Auto.objects.all() #получаем все объекты класса Auto, далее проходимся по каждому полю фильтра и фильтруем объекты которые мы получили
            mark = form.cleaned_data.get('mark')
            if mark != 'all':
                objects = objects.filter(mark=mark)
            model = form.cleaned_data.get('model')
            if model:
                if model != 'all':
                    objects = objects.filter(model=model)
            drive_wheels = form.cleaned_data.get('drive_wheels')
            if drive_wheels != 'ALL':
                dict_wheels = {'4WD': '4WD', 'FWD': 'передний', 'RWD': 'задний'}
                objects = objects.filter(drivewheels=dict_wheels[drive_wheels])
            sorting = form.cleaned_data.get('sorting')
            if sorting != 'ACTUAL':
                if sorting == 'YEAR_OLD':
                    objects = objects.order_by('year')
                if sorting == 'YEAR_NEW':
                    objects = objects.order_by('-year')
                if sorting == 'PRICE_ASC':
                    objects = objects.order_by('price')
                if sorting == 'PRICE_DESC':
                    objects = objects.order_by('-price')
            year_from = form.cleaned_data.get('year_from')
            if year_from:
                objects = objects.filter(year__gte=year_from)
            year_to = form.cleaned_data.get('year_to')
            if year_to:
                objects = objects.filter(year__lte=year_to)
            price_from = form.cleaned_data.get('price_from')
            if price_from:
                objects = objects.filter(price__gte=price_from)
            price_to = form.cleaned_data.get('price_to')
            if price_to:
                objects = objects.filter(price__lte=price_to)
            mileage_from = form.cleaned_data.get('mileage_from')
            if mileage_from:
                objects = objects.filter(milage__gte=mileage_from)
            mileage_to = form.cleaned_data.get('mileage_to')
            if mileage_to:
                objects = objects.filter(milage__lte=mileage_to)
            location = form.cleaned_data.get('location')
            if location:
                if location != 'all':
                    objects = objects.filter(location=location)
            global queryset
            queryset = objects
            paginator = Paginator(objects, 20)  # Show 20 contacts per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'ads/main.html', {'page_obj': page_obj, 'form': form})
    elif queryset:
        form = FilterAds(
            initial={'mark': queryset[0].mark, 'model': queryset[0].model, 'drive_wheels': queryset[0].drivewheels})
        paginator = Paginator(queryset, 20)  #используем пагинатор от Django, выводим 20 объявлений на странице
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'ads/main.html', {'page_obj': page_obj, 'form': form})
    else:
        queryset = None
        form = FilterAds()
        objects = Auto.objects.all()
        paginator = Paginator(objects, 20)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'ads/main.html', {'page_obj': page_obj, 'form': form})


@login_required
def add_to_favourites(request, pk): #добавить в избранное, если нет в избранном то создаем объект модели AdsBookmark и сохраняем
    if AdsBookmark.objects.filter(user=request.user.id, ad=pk):
        messages.info(request, 'Уже в избранном!')
    else:
        new_obj = AdsBookmark(user=request.user.id, ad=pk)
        new_obj.save()
        messages.info(request, 'Добавлено в избранное!')
    return redirect(request.META['HTTP_REFERER'])
