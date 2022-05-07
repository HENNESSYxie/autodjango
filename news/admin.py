from django.contrib import admin
from .models import News

#добавляем модель новостей на админ-панель
admin.site.register(News)
