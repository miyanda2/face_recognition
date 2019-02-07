from django.shortcuts import render
from django.http import HttpResponse
from database import create_table

from .models import Greeting

import logging
logger = logging.getLogger('django.server')

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def db_init(request):
    return render(request, 'db_init.html')

def db_create_table(request):
    if create_table.create():
        logger.info('Table created successfully. views.py')
        return HttpResponse('success')
    else:
        logger.error('Table creation errored. views.py')
        return HttpResponse('error')