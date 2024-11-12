from django.utils import timezone
from django.db import models

# Create your models here.
class Disponibilidad(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    dias = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.fecha} {self.hora} {self.dias}"


class Voluntario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    tipo_voluntario = models.CharField(max_length=50, choices=[
        ('campo', 'Campo'),
        ('acompañador', 'Acompañador'),
        ('recolector', 'Recolector'),
    ])
    disponibilidad = models.ForeignKey(Disponibilidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Donacion(models.Model):
    tipo_donacion = models.CharField(max_length=50, choices=[
        ('ropa', 'Ropa'),
        ('alimentos', 'Alimentos'),
        ('dinero', 'Dinero'),
    ])
    detalles = models.TextField()
    cantidad = models.IntegerField()
    fecha_disponible = models.DateField()
    hora_disponible = models.TimeField()
    confirmacion_enviada = models.BooleanField(default=False)
    foto_comprobante = models.BinaryField(null=True, blank=True)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.tipo_donacion} - {self.cantidad}"


class Informante(models.Model):
    ubicacion = models.TextField()
    evidencia = models.BinaryField(null=True, blank=True)
    solicitud_donacion = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ubicacion


class Reporte(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('Voluntario', 'Voluntario'),
        ('Donador', 'Donador'),
        ('Informante', 'Informante'),
    ]
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO_CHOICES)
    usuario_id = models.IntegerField()
    detalles = models.TextField()
    fecha_reporte = models.DateField(auto_now_add=True)
    voluntario = models.ForeignKey(Voluntario, null=True, blank=True, on_delete=models.SET_NULL)
    donacion = models.ForeignKey(Donacion, null=True, blank=True, on_delete=models.SET_NULL)
    informante = models.ForeignKey(Informante, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Reporte de {self.tipo_usuario}"
    
    CreadoEn = models.DateTimeField(default=timezone.now)