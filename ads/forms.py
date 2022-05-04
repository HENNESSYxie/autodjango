from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, IntegerField
from django import forms
from .models import Auto, AdsBookmark


class FilterAds(ModelForm):
    MARKS = list()
    distinct_marks = Auto.objects.values('mark').distinct()
    MODELS = list()
    distinct_models = Auto.objects.values('model').distinct()
    CITIES = list()
    distinct_cities = Auto.objects.values('location').distinct()
    CITIES.append(('all', 'Россия'))
    MARKS.append(('all', 'Любая марка'))
    MODELS.append(('all', 'Любая модель'))
    for mark in distinct_marks:
        temp = (mark['mark'], mark['mark'])
        MARKS.append(temp)

    for city in distinct_cities:
        temp = (city['location'], city['location'])
        CITIES.append(temp)

    list_of_models_mark = list()
    for i, model in enumerate(distinct_models):
        mark_of_model = Auto.objects.filter(model=model['model'])
        temp_model = mark_of_model[0].model
        if temp_model not in list_of_models_mark:
            list_of_models_mark.append(temp_model)
            temp = (model['model'], f'{mark_of_model[0].mark} {model["model"]}')
            MODELS.append(temp)

    DRIVE_WHEELS = (
        ('--Привод--',
         (
             ('ALL', 'Любой привод'),
             ('4WD', '4WD'),
             ('FWD', 'передний'),
             ('RWD', 'задний'),
         )
         ),
    )
    SORTING_OPTIONS = (
        ('--Сортировка--',
         (
             ('ACTUAL', 'По актуальности'),
             ('YEAR_OLD', 'По году, старше'),
             ('YEAR_NEW', 'По году, новее'),
             ('PRICE_ASC', 'Цена по возрастанию'),
             ('PRICE_DESC', 'Цена по убыванию'),
         )
         ),
    )

    model = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select form-select-sm',
                                                         'aria-label': '.form-select-sm example',
                                                         'disabled': 'true'}), required=False,
                              choices=MODELS)
    mark = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select form-select-sm',
                                                        'aria-label': '.form-select-sm example',
                                                        'onchange': "myFunction(this.value);"}),
                             required=False, choices=MARKS)
    year_from = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'aria-label': 'Год от'}),
                                   required=False)
    year_to = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'aria-label': 'Год до'}),
                                 required=False)
    price_from = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'aria-label': 'Цена от'}),
                                    required=False)
    price_to = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'aria-label': 'Цена до'}),
                                  required=False)
    sorting = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select form-select-sm',
                                                           'aria-label': '.form-select-sm example'}), required=False,
                                choices=SORTING_OPTIONS)
    mileage_from = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'aria-label': 'Пробег от'}),
        required=False)
    mileage_to = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'aria-label': 'Пробег до'}),
        required=False)
    drive_wheels = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select form-select-sm',
                                                                'aria-label': '.form-select-sm example'}),
                                     required=False, choices=DRIVE_WHEELS, label='Привод')
    location = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select form-select-sm',
                                                            'aria-label': '.form-select-sm example'}),
                                 required=False, choices=CITIES)

    class Meta:
        model = Auto
        fields = ['mark', 'model', 'drivewheels', 'location']



