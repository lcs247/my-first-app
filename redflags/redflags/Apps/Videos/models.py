from django.db import models
from django.core.exceptions import ValidationError

 # Create your models here.
def validate_image_extension(foto_casa):
  import os
  ext = os.path.splitext(foto_casa.name)[1]
  valid_extensions = ['.jpg','.png','.jpeg']
  if not ext in valid_extensions:
    raise ValidationError(u'Formato de imagen no válida. Seleccione un archivo de extensión ".jpg" o ".png"')

AYUDAS = [
    ('Alimentos', 'Alimentos'),
    ('Medicinas', 'Medicinas'),
    ('Ropa', 'Ropa'),
    ('Otros', 'Otros'),
]
ESTADO = [
    ('Si','Despachado'),
    ('No','No despachado'),
]

class Ubicacion(models.Model):
    nombre = models.CharField('Nombre y Apellidos de la persona',max_length=35,blank=False)
    direccion = models.CharField('Dirección del domicilio',max_length=70,blank=False)
    telefono = models.CharField('Teléfono de contacto',max_length=10,blank=True)
    latitud =  models.DecimalField('Latitud', max_digits = 20, decimal_places = 18, blank=False)
    longitud = models.DecimalField('Longitud',max_digits = 20, decimal_places = 18, blank=False)
    foto_casa = models.FileField('Fotografía del domicilio',upload_to='',validators=[validate_image_extension], blank=True, null=True)
    tipo_apoyo = models.CharField('Tipo de apoyo',max_length=10, choices=AYUDAS,default='Alimentos',blank=False)
    nro_personas = models.PositiveIntegerField(blank=False)
    estado = models.CharField('Estado', max_length=2, choices=ESTADO, default='No despachado')
    ingresado = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modificado = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)
    comentario = models.CharField('Comentarios',max_length=200,default='',blank=True)
