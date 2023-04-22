from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    REQUIRED_FIELDS = ['email', 'contraseña']


class Articulos(models.Model):
    nombre = models.CharField(max_length=100)
    seccion = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

class Posts(models.Model):
    imagen = models.ImageField(upload_to='images', null=True, blank=True)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField()

class hilo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField()