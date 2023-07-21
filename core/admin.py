from django.contrib import admin
from .models import Vacancy
from .models import Company
from .models import Category
from .models import Skill



# Register your models here.


admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Skill)



