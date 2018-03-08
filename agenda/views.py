from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def agenda_view(request):
    loginUser = request.user
    return render(request,'agenda_contactos_template.html',{'loginUser': loginUser})