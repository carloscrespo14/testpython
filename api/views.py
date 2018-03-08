from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from agenda.models import Contacto
from api.serializers import ContactoSerializer, ContactoCreateSerializer

class ContactoCreateAPIView(CreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    
class ContactoDetailAPIView(RetrieveAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    #lookup_field = 'cowner'
    #lookup_url_kwarg = 'abc'

class ContactoUpdateAPIView(UpdateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    #lookup_field = 'cowner'
    #lookup_url_kwarg = 'abc'    

class ContactoDeleteAPIView(RetrieveAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    #lookup_field = 'cowner'
    #lookup_url_kwarg = 'abc'

class ContactoListAPIView(ListAPIView):
    serializer_class = ContactoSerializer
    queryset = Contacto.objects.all()