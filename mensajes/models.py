from django.db import models

# Create your models here.
#encoding:utf-8
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.datetime_safe import date
from django.utils import timezone
from miembros.models import Miembro
from usuarios.models import Usuario
from proyectos.models import Proyecto
# Create your models here.

class Mensaje(models.Model):
    proyecto = models.ForeignKey(Proyecto, unique=False)
    remitente = models.ForeignKey(Usuario, unique=False)
    destinatario = models.ForeignKey(Miembro, unique=False,help_text='a quien envia')
    texto_mensaje = models.TextField(max_length=1000, help_text='Escriba aqui su mensaje', null=True)
    fecha_hora_creacion = models.DateTimeField(default=date.today(), help_text='Hora de envio del mensaje', null=True)

    def __unicode__(self):
       return self.remitente.usuario.username

