from django.urls import path
from .views import *


urlpatterns = [
    path('article/', NewsListView.as_view(), name='article_list'),
    path('article/<int:pk>/', NewsDetailView.as_view(), name='article_detail'),
    path('article-add/', NewsCreateView.as_view(), name='article_add'),
    path('article-update/<int:pk>/', NewsUpdateView.as_view(), name='article_update'),

]
