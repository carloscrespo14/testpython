from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def agenda_view(request):
    return HttpResponse('Agenda')