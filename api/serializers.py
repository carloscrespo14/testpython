from rest_framework import serializers
from agenda.models import Contacto, Telefono, Social

class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = ('tipo', 'numero')

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('red', 'urln')        

class ContactoSerializer(serializers.ModelSerializer):
    telefono = TelefonoSerializer(many=True)
    social = SocialSerializer(many=True)

    class Meta:
        model = Contacto
        fields = (
            'id',
            'nombre',
            'apellidos',
            'organizacion',
            'cowner',
            'telefono',
            'social'
            )

class ContactoCreateSerializer(serializers.ModelSerializer):
    telefono = TelefonoSerializer(many=True)
    social = SocialSerializer(many=True)
    class Meta:
        model = Contacto
        fields = (
            'id',
            'nombre',
            'apellidos',
            'organizacion',
            'telefono',
            'social'
        )

    def create(self, validated_data):
        telefono_data = validated_data.pop('telefono')
        social_data = validated_data.pop('social')
        contacto = Contacto.objects.create(**validated_data)
        for telefono_data in telefono_data:
            Telefono.objects.create(contacto=contacto, **telefono_data)
        for social_data in social_data:
            Social.objects.create(contacto=contacto, **social_data)    
        return contacto    



class ContactoUpdateSerializer(serializers.HyperlinkedModelSerializer):
    telefono = serializers.StringRelatedField(many=True)
    social = serializers.StringRelatedField(many=True)
    class Meta:
        model = Contacto
        fields = (
            'id',
            'nombre',
            'apellidos',
            'organizacion',
            'telefono',
            'social'
        )

