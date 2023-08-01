from django.contrib import admin
from .models import Vacancy
from .models import Company
from .models import Category
from .models import Skill

# Register your models here.


# admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Skill)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'salary', 'is_relevant', 'contacts']
    search_fields = ['title', 'description', 'candidate__name']
    list_filter = ['category', 'salary', 'is_relevant']
    list_editable = ['is_relevant', 'contacts']
