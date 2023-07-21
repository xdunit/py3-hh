import django_filters
from .models import Vacancy


class VacancyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')
    experience__gt = django_filters.NumberFilter(field_name='experience', lookup_expr='gt')
    experience__lt = django_filters.NumberFilter(field_name='experience', lookup_expr='lt')
    employment_type = django_filters.ChoiceFilter(choices=Vacancy.EMPLOYMENT_TYPE_CHOICES)
    skill_name = django_filters.CharFilter(field_name='skill_name__skill_name', lookup_expr='icontains',
                                           label='Skill name содержит:')

    class Meta:
        model = Vacancy
        fields = ['title', 'employment_type', 'experience', 'skill_name']
