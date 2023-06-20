from django.shortcuts import render, HttpResponse


# Create your views here.

def homepage(request):
    return HttpResponse('hi')


def about(request):
    return HttpResponse('Найдите работу или работника мечты')


def contacts(request):
    return HttpResponse(f'Phone: +996777123456 <br> Email: office@handhunter.kg')


def address(request):
    return HttpResponse('<ul> <li>test@mail.com</li> <li>test2@mail.com</li> </ul>'
                        '<ol> <li>test@mail.com</li> <li>test2@mail.com</li> </ol>')

