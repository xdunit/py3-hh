"""
URL configuration for handhunter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
from worker.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about/', about),
    path('contacts/', contacts),
    path('address/', address),
    path('vacancies/', vacancy_list),
    path('companies/', company_list),
    path('workers/', workers_list),
    path('worker/<int:id>/', worker_info),
    path('resume-list/', resume_list),
    path('resume-info/<int:id>/', resume_info),
    path('my-resume/', my_resume, name='my-resume'),
    path('vacancy/<int:id>/', vacancy_details),
    path('search/', search, name='search'),
    path('add-resume/', add_resume, name='add-resume'),
    path('registration/', reg_view, name='reg'),
    path('add-vacancy/', add_vacancy, name='add_vacancy'),
    path('vacancy-edit/<int:id>/', vacancy_edit, name='vacancy-edit'),
    path('resume-edit/<int:id>/', resume_edit, name='resume-edit'),
    path('add-vacancy-df/', vacancy_add_via_django_form, name='add-vacancy-df'),
    path('edit-resume-django', edit_resume_django, name='edit-resume-django')

]
