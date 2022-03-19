from rest_framework import serializers
from .models import Finca, ControlBultos, ControlBultosDetalle, Pilon, Clase, Corte, Variedad


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


class BultoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlBultos
        fields = '__all__'


class DisableBultoSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(required=True)

    class Meta:
        model = ControlBultos
        fields = ['estado']


class BultoDetallesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlBultosDetalle
        fields = '__all__'

    # def to_representation(self, instance):
    #    response = super().to_representation(instance)
    #    response['controlbultos'] = BultoSerializer(instance.id).data
    #    return response


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
