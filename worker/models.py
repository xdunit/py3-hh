from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Worker(models.Model):
    user = models.OneToOneField(to=User, null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    expected_salary = models.SmallIntegerField(null=False)
    is_searching = models.BooleanField(default=True, verbose_name='Ищет работу?')

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(to=Worker, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username


class Resume(models.Model):
    name = models.ForeignKey(to=Worker, on_delete=models.CASCADE)
    age = models.SmallIntegerField(null=False)
    specialization = models.CharField(max_length=255)
    info = models.TextField(verbose_name='Расскажите о себе')
    profile_photo = models.ImageField(null=True, blank=True, upload_to='profile_photo/',
                                      verbose_name='Фото сотрудника')

    def __str__(self):
        return self.specialization




