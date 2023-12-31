from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Recruiter(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='recruiter')
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    payment_for_found = models.IntegerField(null=True, blank=True)
    bonus_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.user.username


