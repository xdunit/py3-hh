from django.contrib import admin
from .models import Worker, Comment, Resume

# Register your models here.

admin.site.register(Worker)
admin.site.register(Comment)
admin.site.register(Resume)
