from rest_framework import serializers
from agenda.models import Contacto

class ContactoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacto
        fields = [
            'id',
            'nombre',
            'apellidos',
            'organizacion',
            'cowner',
        ]

class ContactoCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacto
        fields = [
            'nombre',
            'apellidos',
            'organizacion',
            'cowner',
        ]
