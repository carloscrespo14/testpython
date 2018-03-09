from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellidos = models.CharField(max_length=50, null=True, blank=True)
    organizacion = models.CharField(max_length=50, null=True, blank=True)
    correo = models.CharField(max_length=50, null=True, blank=True)
    owner = models.CharField(max_length=50, null=True, blank=True)
  
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
    towner = models.ForeignKey(Contacto, related_name='telefono', null=True, blank=True, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20, null=True, blank=True)
    tipo = models.CharField(max_length=20, null=True, blank=True, choices=PHONE_TYPE)

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
    sowner = models.ForeignKey(Contacto, related_name='social', null=True, blank=True, on_delete=models.CASCADE)
    urln = models.CharField(max_length=100, null=True, blank=True)
    red = models.CharField(max_length=20, null=True, blank=True, choices=SOCIAL_NETWORK)

    def __str__(self):
        return '{} {}'.format(self.red, self.urln)