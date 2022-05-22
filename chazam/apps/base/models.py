from django.db import models

# Create your models here.
class categoria(models.Model):
    IdCategoria = models.AutoField(primary_key=True)
    IdChaza = models.ForeignKey(chaza, on_delete=models.CASCADE)
    NombreCategoria = models.CharField(max_length=20, blank=False, null=False)

class chaza(models.Model):
    IdChaza = models.AutoField(primary_key=True)
    NombreChaza = models.CharField(max_length=40, blank=False, null=False)
    Puntuacion = models.FloatField(blank=False, null=False)
    Descripcion = models.TextField(blank=False, null=False)
    Ubicacion = models.CharField(max_length=200, blank=False, null=False)

class comensales(models.Model):
    IdComensal = models.AutoField(primary_key=True)
    IdTipoUsuario = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE)
    NombreUsuario = models.CharField(max_length=20, blank=False, null=False)
    Email = models.CharField(max_length=30, blank=False, null=False)
    Contrasena = models.CharField(max_length=40, blank=False, null=False)

class comentarios(models.Model):
    IdComentario = models.AutoField(primary_key=True)
    IdComensal = models.ForeignKey(comensales, on_delete=models.CASCADE)
    IdChaza = models.ForeignKey(chaza, on_delete=models.CASCADE)
    DescripcionComentario= models.TextField(max_length=400, blank=False, null=False)

class DuenoChaza(models.Model):
    IdDuenoChaza = models.AutoField(primary_key=True)
    IdComensal = models.ForeignKey(comensales, on_delete=models.CASCADE)

class Producto(models.Model):
    IdProducto = models.AutoField(primary_key=True)
    IdChaza = models.ForeignKey(chaza, on_delete=models.CASCADE)
    NombreProducto = models.CharField(max_length=30, blank=False, null=False)
    Precio = models.FloatField(blank=False, null=False)
    Imagen = models.ImageField()

class tipoUsuario(models.Model):
    IdTipoUsuario = models.AutoField(primary_key=True)
    NombreTipoUsuario = models.CharField(max_length=30, blank=False, null=False)



    
