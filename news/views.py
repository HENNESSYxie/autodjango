from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView
from .models import News


#отображение главной страницы вкладки новостей, получаем все новости и используя пагинатор выводим их на странице
def news(request):
    objs = News.objects.all()
    paginator = Paginator(objs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ads/news.html', {'page_obj': page_obj})


class NewsDetailView(DetailView): #детальное отображение новости id
    model = News
    template_name = 'ads/news-inner.html'
    context_object_name = 'news'
