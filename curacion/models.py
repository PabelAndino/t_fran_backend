from django.db import models


class Pilon(models.Model):
    numero = models.IntegerField(null=False)

class Finca(models.Model):
    nombre = models.CharField(max_length=300, null=False)
    descripcion = models.TextField(max_length=500)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modifica = models.DateField(null=True)
    estado = models.BooleanField(default=True)


class ControlBultos(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING)
    fecha = models.DateField(auto_now_add=True)
    observacion = models.TextField(max_length=400, blank=True)
    estado = models.BooleanField(default=True)


class ControlBultosDetalle(models.Model):
    pilon = models.IntegerField()
    libras = models.DecimalField(max_digits=5, decimal_places=2)
    clase = models.CharField(max_length=100)
    corte = models.CharField(max_length=100)
    bulto = models.ForeignKey(ControlBultos, on_delete=models.DO_NOTHING)
    # Control de pilones
