from django.db.models import query
from django.shortcuts import render
from . models import todoModel


def home(request):

    return render(request, 'main/index.html', context)