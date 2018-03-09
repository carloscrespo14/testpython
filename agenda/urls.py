from django.urls import path
from agenda.views import ContactoDelete
from . import views

app_name = 'agenda'

urlpatterns = [
    #path('',views.agenda_view, name='lista'),
    path('',views.AgendaLista.as_view(), name='lista')
    path('agregar/',views.AgregarView.as_view(), name='agregar'),
    path('eliminar/<pk>', views.ContactoDelete.as_view(), name='eliminar'),
]