from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import ArticleNew
from .forms import NewsUpdateForm

# Create your views here.


class NewsDetailView(View):
    @staticmethod
    def get(request, pk):
        news_detail = get_object_or_404(ArticleNew, pk=pk)
        news_detail.views_count += 1
        news_detail.save()

        return render(request, 'article/news_detail.html', {'news_detail': news_detail})


class NewsListView(ListView):
    model = ArticleNew
    template_name = 'article/news_list.html'


class NewsCreateView(CreateView):
    model = ArticleNew
    template_name = 'article/news_form.html'
    fields = ['author', 'title', 'text']

    def get_success_url(self):
        return reverse('article_list')


class NewsUpdateView(UpdateView):
    model = ArticleNew
    form_class = NewsUpdateForm
    template_name = 'article/news_form.html'
    success_url = reverse_lazy('article_list')

