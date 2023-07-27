from django.db import models

# Create your models here.
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=20)
    hecho = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre+' - '+self.proyecto.nombre