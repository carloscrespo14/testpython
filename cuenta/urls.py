from django.urls import path
from . import views

app_name = 'cuenta'

urlpatterns = [
    path('',views.cuenta_registro_view, name='registro_usuarios')  
]