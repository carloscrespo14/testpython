from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    organizacion = models.CharField(max_length=50)
    cowner = models.CharField(max_length=50)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.apellidos, self.organizacion)

class Telefono(models.Model):
    PHONE_TYPE = (
        ('C', 'Celular'),
        ('P', 'Particular'),
        ('L', 'Laboral'),
        ('F', 'Principal'),
        ('O', 'Otros'),
    )
    towner = models.ForeignKey(Contacto, null=True, blank=True, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    tipo = models.CharField(max_length=1, choices=PHONE_TYPE)

    def __str__(self):
        return '{} {}'.format(self.tipo, self.numero)
   
class Social(models.Model):
    SOCIAL_NETWORK = (
        ('FB', 'Facebook'),
        ('TW', 'Twitter'),
        ('IN', 'Instagram'),
        ('YT', 'Youtbe'),
        ('OT', 'Otros'),
    )
    sowner = models.ForeignKey(Contacto, null=True, blank=True, on_delete=models.CASCADE)
    urln = models.CharField(max_length=100)
    red = models.CharField(max_length=2, choices= SOCIAL_NETWORK)

    def __str__(self):
        return '{} {}'.format(self.red, self.urln)