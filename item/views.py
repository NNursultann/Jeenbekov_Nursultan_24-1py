from django.shortcuts import HttpResponse

# Create your views here.

def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')

def now_date(request):
    if request.method == 'GET':
        return HttpResponse('now date: 13.01.2023')

def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')