from django.urls import path
from . import views

urlpatterns = [
    path('',views.agenda_view, name='lista')
]