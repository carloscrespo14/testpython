from django.db.models import Q

from rest_framework.generics import (
    RetrieveUpdateAPIView, 
    RetrieveDestroyAPIView, 
    CreateAPIView, 
    ListAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView
)

from rest_framework.filters import SearchFilter, OrderingFilter

from agenda.models import Contacto
from api.serializers import ContactoSerializer, ContactoCreateSerializer, ContactoUpdateSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class ContactoCreateAPIView(CreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoCreateSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        serializer.save(cowner=self.request.user)
    
class ContactoDetailAPIView(RetrieveAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    permission_classes = [AllowAny]

class ContactoUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoUpdateSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save(cowner=str(self.request.user))
     

class ContactoDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    permission_classes = [AllowAny]


class ContactoListAPIView(ListAPIView):
    serializer_class = ContactoSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id','nombre', 'apellidos', 'organizacion', 'cowner']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Contacto.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(id__icontains=query)|
                Q(nombre__icontains=query)|
                Q(apellidos__icontains=query)|
                Q(organizacion__icontains=query)|
                Q(cowner__icontains=query)
                ).distinct()
        return queryset_list        
          