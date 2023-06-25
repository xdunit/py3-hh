from django.shortcuts import render
from .models import Worker


# Create your views here.


def workers_list(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'workers.html', context)


def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)  # SELECT * FROM Worker WHERE id = id
    context = {'worker': worker_object}
    vacancies = worker_object.vacancy_set.all()
    return render(request, 'worker.html', context)
