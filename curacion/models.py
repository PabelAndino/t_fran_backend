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
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modifica = models.DateField(null=True)
    estado = models.BooleanField(default=True)


class Variedad(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    estado = models.BooleanField(default=True)


class ControlBultos(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING)
    fecha = models.DateField(auto_now_add=True)
    observacion = models.TextField(max_length=400, blank=True)
    pilon = models.ForeignKey(Pilon, on_delete=models.DO_NOTHING)
    condicion = models.IntegerField(default=1)
    estado = models.BooleanField(default=True)


class ControlBultosDetalle(models.Model):
    libras = models.DecimalField(max_digits=5, decimal_places=2)
    clase = models.ForeignKey(Clase, on_delete=models.DO_NOTHING)
    corte = models.ForeignKey(Corte, on_delete=models.DO_NOTHING)
    bulto = models.ForeignKey(ControlBultos, on_delete=models.DO_NOTHING)


class ControlTemperaturaBultos(models.Model):
    fecha = models.DateField()
    bulto = models.ForeignKey(ControlBultos, on_delete=models.DO_NOTHING)
    finca = models.ForeignKey(Finca, on_delete=models.DO_NOTHING)
    variedad = models.ForeignKey(Variedad, on_delete=models.DO_NOTHING)
    corte = models.ForeignKey(Corte, on_delete=models.DO_NOTHING)
    ciclo = models.IntegerField()
    temperatura = models.DecimalField(max_digits=4, decimal_places=2)
    estado = models.BooleanField(default=True)
