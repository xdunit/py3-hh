from django.shortcuts import render, HttpResponse, redirect
from .models import Vacancy
from .models import Company
from .forms import VacancyForm
from django.contrib.auth.models import User


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


def reg_view(request):
    if request.method == 'POST':
        user = User(
            username=request.POST['username']
        )
        user.save()
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponse('Готово')

    return render(request, 'auth/registr.html')


def add_vacancy(request):
    if request.method == 'POST':
        new_vacancy = Vacancy(
            title=request.POST['title'],
            salary=int(request.POST['salary']),
            description=request.POST['description'],
            is_relevant=request.POST['is_relevant'],
            email=request.POST['email'],
            contacts=request.POST['contacts'],
        )
        new_vacancy.save()
        return redirect(f'/vacancy/{new_vacancy.id}/')

    return render(request, 'vacancy/add_vacancy.html')


def vacancy_add_via_django_form(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            new_vacancy = form.save()
            return redirect(f'/vacancy/{new_vacancy.id}')

    vacancy_form = VacancyForm()
    return render(request, 'vacancy/vacancy_django_form.html', {'vacancy_form': vacancy_form})


def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.method == 'POST':
        vacancy.title = request.POST['title']
        vacancy.salary = int(request.POST['salary'])
        vacancy.description = request.POST['description']
        vacancy.is_relevant = request.POST['is_relevant']
        vacancy.email = request.POST['email']
        vacancy.contacts = request.POST['contacts']
        vacancy.save()
        return redirect(f'/vacancy/{vacancy.id}/')

    return render(request, 'vacancy/vacancy_edit_form.html', {'vacancy': vacancy})
