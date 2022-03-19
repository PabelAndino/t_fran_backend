from django.db import models


class Pilon(models.Model):
    nombre = models.IntegerField(null=False)
    estado = models.BooleanField(default=True)


class Corte(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    estado = models.BooleanField(default=True)


class Clase(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    estado = models.BooleanField(default=True)


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
    clase = models.ForeignKey(Clase, on_delete=models.DO_NOTHING)
    corte = models.ForeignKey(Corte, on_delete=models.DO_NOTHING)
    bulto = models.ForeignKey(ControlBultos, on_delete=models.DO_NOTHING)
    # Control de pilones


class Variedad(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    estado = models.BooleanField(default=True)
