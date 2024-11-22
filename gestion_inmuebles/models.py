from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Region(models.Model):
    nombre_region = models.CharField(max_length=100)
    numero_region = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas')

    def __str__(self):
        return self.nombre_comuna    
    
class Perfil(models.Model):
    TIPO_USUARIO = [
        ('Arrendatario', 'Arrendatario'),
        ('Arrendador', 'Arrendador')
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    tipo_usuario = models.CharField(max_length=12, choices=TIPO_USUARIO)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.tipo_usuario}"

class Inmueble(models.Model):
    TIPO_INMUEBLE = [
        ('Casa', 'Casa'),
        ('Departamento', 'Departamento'),
        ('Parcela', 'Parcela')
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    metros_construidos = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
        )
    metros_totales = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)]
    )    
    cantidad_estacionamientos = models.IntegerField(validators=[MinValueValidator(1)])
    cantidad_habitaciones = models.IntegerField(validators=[MinValueValidator(1)])
    cantidad_banos = models.IntegerField(validators=[MinValueValidator(1)])
    direccion = models.CharField(max_length=255)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True)
    tipo_inmueble = models.CharField(max_length=20, choices=TIPO_INMUEBLE)
    precio_mensual = models.DecimalField(max_digits=12, decimal_places=2,validators=[MinValueValidator(0.01)])
    arrendador = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='propiedades')
    fecha_creacion = models.DateTimeField(auto_now_add=True)  
    ultima_modificacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='static/', null=True, blank=True)



    def __str__(self):
        return f"{self.nombre} - {self.tipo_inmueble} en {self.comuna}"
