from django.shortcuts import render

# Create your views here.

def cuenta_registro_view(request):
    return render(request,'cuenta_registro_template.html')
