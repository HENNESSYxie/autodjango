from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView
from .models import News


def news(request):
    objs = News.objects.all()
    paginator = Paginator(objs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ads/news.html', {'page_obj': page_obj})


class NewsDetailView(DetailView):
    model = News
    template_name = 'ads/news-inner.html'
    context_object_name = 'news'
