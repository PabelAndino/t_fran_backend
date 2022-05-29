from rest_framework import serializers
from .models import Finca, ControlBultos, ControlBultosDetalle, Pilon, Clase, Corte, Variedad, ControlTemperaturaBultos


class FincaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finca
        fields = '__all__'


class FincaPatchSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=False)
    descripcion = serializers.CharField(required=False)

    class Meta:
        model = Finca
        fields = '__all__'


class FincaDisableSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = Finca
        fields = ['estado']


class FincaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finca
        fields = ['id', 'nombre']


class PilonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finca
        fields = ['id', 'nombre']


class BultoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlBultos
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['finca'] = FincaDetailSerializer(instance.finca).data
        response['pilon'] = PilonDetailSerializer(instance.pilon).data
        return response


class DisableBultoSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = ControlBultos
        fields = ['estado']


class ClaseForDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'nombre']


class CorteForDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corte
        fields = ['id', 'nombre']


class BultoDetallesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlBultosDetalle
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['clase'] = ClaseForDetailSerializer(instance.clase).data
        response['corte'] = CorteForDetailSerializer(instance.corte).data
        return response


class BultoDetallesDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlBultosDetalle
        fields = ['id']


class PilonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilon
        fields = '__all__'


class PilonDisableSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = Pilon
        fields = ['estado']


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'


class DisableClaseSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = Clase
        fields = ['estado']


class CorteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corte
        fields = '__all__'


class DisableCorteSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = Corte
        fields = ['estado']


class VariedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variedad
        fields = '__all__'


class DisableVariedadSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = Variedad
        fields = ['estado']


class TemperaturaBultoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlTemperaturaBultos
        fields = '__all__'


class DisableTemperaturaSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = ControlTemperaturaBultos
        fields = ['estado']
