from django.db import models
from worker.models import Worker
from django.contrib.auth.models import User


# Create your models here.

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name


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
    experience = models.IntegerField(null=True, blank=True)

    FULL_TIME = 'full'
    PART_TIME = 'part'
    COMPLETED_WORK = 'comp'
    EMPLOYMENT_TYPE_CHOICES = [
        (FULL_TIME, 'Полный рабочий день'),
        (PART_TIME, 'Частичная занятость'),
        (COMPLETED_WORK, 'Сделанная работа')
    ]

    employment_type = models.CharField(
        max_length=4,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default=FULL_TIME
    )
    skill_name = models.ManyToManyField(to=Skill, blank=True)

    def __str__(self):
        return {self.title} - {self.employment_type}

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['salary']
        unique_together = [['title', 'email']]


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)
    founding_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=255)
    workers = models.ManyToManyField(to=Worker)
    employees_num = models.SmallIntegerField(null=False)
    is_hunting = models.BooleanField(default=True, verbose_name='Есть вакансии?')

    def __str__(self):
        return self.name



