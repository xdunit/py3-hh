from django.shortcuts import render
from .models import Worker
from .models import Resume


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
    resume_query = Resume.objects.all()
    return render(request, 'resume/resume_list.html',
                  {"resumes": resume_query}
                  )


def resume_info(request, id):
    resume_object = Resume.objects.get(id=id)
    return render(request, 'resume/resume_detail.html',
                  {'resume': resume_object}
                  )


def my_resume(request):
    resume_query = Resume.objects.filter(name=request.user.worker)
    return render(request, 'resume/resume_list.html',
                  {"resumes": resume_query}
                  )
