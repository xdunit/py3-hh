from django.db import models


# Create your models here.


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='Нет описания')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    employees_num = models.SmallIntegerField(null=False)
    is_hunting = models.BooleanField(default=True, verbose_name='Есть вакансии?')

    def __str__(self):
        return self.name




