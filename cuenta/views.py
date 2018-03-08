from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from cuenta.forms import registroForm

# Create your views here.

def cuenta_registro_view(request):
    if request.method == 'POST':
        form = registroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
    else:        
        form = registroForm()
    return render(request,'cuenta_registro_template.html')
