from django.shortcuts import render, HttpResponse
from .models import Vacancy
from .models import Company


# Create your views here.


def homepage(request):
    return render(request=request, template_name="index.html")


def about(request):
    return HttpResponse('Найдите работу или работника мечты')


def contacts(request):
    return HttpResponse(f'Phone: +996777123456 <br> Email: office@handhunter.kg')


def address(request):
    return HttpResponse('<ul> <li>test@mail.com</li> <li>test2@mail.com</li> </ul>'
                        '<ol> <li>test@mail.com</li> <li>test2@mail.com</li> </ol>')


def vacancy_list(request):
    vacancies = Vacancy.objects.all()  # SELECT in django ORM
    context = {'vacancies': vacancies}  # context data for jinja2
    # context['example'] = 'hello world'
    return render(request, 'vacancies.html', context)


def company_list(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'companies.html', context)


def vacancy_details(request, id):
    vacancy = Vacancy.objects.get(id=id)
    candidates = vacancy.candidate.all()
    context = {'vacancy': vacancy,
               'candidates': candidates}

    return render(request, 'v_details/v_details.html', context)


def search(request):
    word = request.GET["keyword"]
    vacancy_list = Vacancy.objects.filter(title__contains=word)
    context = {'vacancies': vacancy_list}
    return render(request, 'vacancies.html', context)


