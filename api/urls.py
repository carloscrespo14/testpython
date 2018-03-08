from django.urls import path
from . import views

urlpatterns = [
    path('',views.ContactoListAPIView.as_view(), name='lista_contactos'),
    path('create',views.ContactoCreateAPIView.as_view(), name='crear_contacto'),
    path('<pk>',views.ContactoDetailAPIView.as_view(), name='detalle_contacto'),
    path('<pk>/edit/',views.ContactoUpdateAPIView.as_view(), name='update_contacto'),
    path('<pk>/delete/',views.ContactoDeleteAPIView.as_view(), name='delete_contacto'),

]