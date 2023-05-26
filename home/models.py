from django.db import models

# Create your models here.
class Temporada(models.Model):
    video = models.FileField(upload_to='videos')
    titulo= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=100)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'temporada'
        verbose_name_plural = 'temporadas'

    def __str__(self):
        return self.titulo
    

class Bloc(models.Model):
    imagen=models.ImageField(upload_to='bloc')
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='blog'
        verbose_name_plural='blogs'

    def __str__(self):
        return self.titulo


class Descarga(models.Model):
    imagen=models.ImageField(upload_to='descarga')
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='descarga'
        verbose_name_plural='descargas'

    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    imagen = models.ImageField(upload_to='contacto/', null=True, blank=True)
    nombre_completo = models.CharField(max_length=100)
    habilidades = models.TextField()
    ubicacion = models.CharField(max_length=100)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    whatsapp = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)