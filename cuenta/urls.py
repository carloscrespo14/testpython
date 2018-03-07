from django.urls import path
from . import views

urlpatterns = [
    path('',views.cuenta_registro_view, name='registro_usuarios')
]