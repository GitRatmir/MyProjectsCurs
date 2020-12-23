from django.shortcuts import render
from django.http import HttpResponse
from .models import Student



def index(request):
    context = {
        'title': 'Главная страница сайта',
        'students': Student.objects.all(),
    }
    return render(request, 'main/index.html', context)
# Create your views here.
