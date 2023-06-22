from django.db import models

# Create your models here.


class Worker(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    expected_salary = models.SmallIntegerField(null=False)
    is_searching = models.BooleanField(default=True, verbose_name='Ищет работу?')

    def __str__(self):
        return self.name
