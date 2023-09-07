from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ArticleNew(models.Model):
    author = models.ForeignKey(
        to=User,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='article_new_object'
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.PositiveIntegerField(default=0)
    likes_users = models.ManyToManyField(to=User, blank=True)


class NewsView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleNew, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)
