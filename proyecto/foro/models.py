from django.db import models
from django.contrib.auth.models import User

class Consola(models.Model):
    consolaseleccion = (
    ('xbox','Xbox'),
    ('switch','Nintendo_Switch'),
    ('ps4','PS4'),
    ('pc','PC'),
    ('otro','Otro'),
    )
    productoseleccion = (
    ('consola','Consola'),
    ('juego','Juego'),
    ('periferico','Periferico'),
    )
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    consola = models.CharField(max_length=15, choices=consolaseleccion, default='pc')
    producto = models.CharField(max_length=15, choices=productoseleccion, default='juego')
    descripcion = models.TextField(null=True, blank=True)
    año = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="juegos/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario = models.ForeignKey('Consola', related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)