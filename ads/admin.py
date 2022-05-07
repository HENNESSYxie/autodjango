from django.contrib import admin
from .models import Auto
from .models import AdsBookmark

#добавляем модели в админ панельку
admin.site.register(Auto)
admin.site.register(AdsBookmark)
