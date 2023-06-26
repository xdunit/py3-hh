from django.db import models
from worker.models import Worker
from django.contrib.auth.models import User


# Create your models here.


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='Нет описания')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    candidate = models.ManyToManyField(to=Worker, blank=True)
    review = models.ManyToManyField(to=User, blank=True)
    category = models.ForeignKey(to='Category', null=True, blank=False, verbose_name='категория',
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['salary']


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    employees_num = models.SmallIntegerField(null=False)
    is_hunting = models.BooleanField(default=True, verbose_name='Есть вакансии?')

    def __str__(self):
        return self.name
