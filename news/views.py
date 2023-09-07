from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import *
from .forms import NewsUpdateForm

# Create your views here.


class NewsDetailView(View):
    @staticmethod
    def get(request, pk):
        news_detail = get_object_or_404(ArticleNew, pk=pk)
        if not NewsView.objects.filter(user=request.user, article=news_detail).exists():
            news_detail.views_count += 1
            news_detail.save()
            NewsView.objects.create(user=request.user, article=news_detail)

        is_liked = False
        if request.user.is_authenticated:
            is_liked = news_detail.likes_users.filter(id=request.user.id).exists()

        return render(request, 'article/news_detail.html', {'news_detail': news_detail, 'is_liked': is_liked})

    @staticmethod
    def post(request, pk):
        news_detail = get_object_or_404(ArticleNew, pk=pk)

        if request.user.is_authenticated:
            if 'like' in request.POST:
                news_detail.likes_users.add(request.user)
            elif 'unlike' in request.POST:
                news_detail.likes_users.remove(request.user)

        return redirect('article_detail', pk=pk)


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

