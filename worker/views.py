from django.shortcuts import render, redirect, HttpResponse
from .models import Worker
from .models import Resume
from .forms import ResumeEditForm
from .forms import ResumeAdd


# Create your views here.


def workers_list(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'workers.html', context)


def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)  # SELECT * FROM Worker WHERE id = id
    vacancies = worker_object.vacancy_set.all()
    context = {'worker': worker_object,
               'vacancies': vacancies}
    return render(request, 'worker.html', context)


def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resume/resume_list.html', {'resumes': resumes})


def resume_info(request, id):
    resume_object = Resume.objects.get(id=id)
    return render(request, 'resume/resume_detail.html',
                  {'resume': resume_object}
                  )


def my_resume(request):
    if request.user.is_authenticated:
        resume_query = Resume.objects.filter(name=request.user.worker)
        return render(request, 'resume/resume_list.html',
                      {"resumes": resume_query}
                      )
    else:
        return redirect('homepage')


def add_resume(request):
    template = 'resume/resume_add.html'
    if request.method == "GET":
        return render(request, template)
    elif request.method == 'POST':
        new_resume = Resume()
        new_resume.name = request.user.worker
        new_resume.age = request.POST['form-age']
        new_resume.specialization = request.POST['form-spec']
        new_resume.info = request.POST['form-info']
        new_resume.save()
        return HttpResponse('added')


def resume_edit(request, id):
    resume = Resume.objects.get(id=id)
    if request.method == 'POST':
        resume.name.name = request.POST['name']
        resume.age = int(request.POST['age'])
        resume.specialization = request.POST['specialization']
        resume.info = request.POST['info']
        resume.name.save()
        resume.save()
        return redirect(f'/resume-info/{resume.id}/')

    return render(request, 'resume/resume_edit.html', {'resume': resume})


def edit_resume_django(request, id):
    resume_object = Resume.objects.get(id=id)

    if request.method == "GET":
        form = ResumeEditForm(instance=resume_object)
        return render(request, "resume/edit_resume_django.html", {"form": form})

    elif request.method == "POST":
        form = ResumeEditForm(data=request.POST, instance=resume_object)
        if form.is_valid():
            obj = form.save()
            return redirect('resume_info', id=obj.id)
        else:
            return HttpResponse("Форма не валидна")


def add_resume_django(request):
    if request.method == 'POST':
        add_resume_form = ResumeAdd(request.POST)
        if add_resume_form.is_valid():
            new_resume = add_resume_form.save()
            return redirect('resume-info', id=new_resume.id)

    add_resume_form = ResumeAdd()
    return render(request, 'resume/add_resume_django.html', {'add_resume_form': add_resume_form})


