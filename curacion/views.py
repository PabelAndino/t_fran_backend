from drf_yasg.utils import swagger_auto_schema
from django.db import IntegrityError
from rest_framework.decorators import api_view, action
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import FincaSerializer, FincaPatchSerializer, FincaDisableSerializer, BultoSerializer, \
    DisableBultoSerializer, BultoDetallesSerializer, PilonSerializer, PilonDisableSerializer, ClaseSerializer, \
    DisableClaseSerializer, CorteSerializer, DisableCorteSerializer, VariedadSerializer, \
    BultoDetallesDeleteSerializer, DisableVariedadSerializer, TemperaturaBultoSerializer, DisableTemperaturaSerializer
from .models import Finca, ControlBultos, ControlBultosDetalle, Pilon, Clase, Corte, Variedad, ControlTemperaturaBultos


class FincaViewSet(viewsets.ViewSet):

    @swagger_auto_schema(request_body=FincaSerializer)  # para que muestre los parametros
    def create(self, request):
        try:
            serializer = FincaSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Finca Guardad correctamente"}
        except:
            dict_response = {"error": True, "details": serializer.errors}
        return Response(dict_response)

    def list(self, request):
        finca = Finca.objects.filter(estado=True)
        serializer = FincaSerializer(finca, many=True, context={'request': request})
        response_dic = {
            'error': False,
            'message': 'Todas las fincas ',
            'data': serializer.data
        }

        return Response(response_dic)

    @swagger_auto_schema(request_body=FincaDisableSerializer)
    @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', name='Disable Finca')
    def disable_finca(self, request, pk=None):
        try:
            query_set = Finca.objects.all()
            finca = get_object_or_404(query_set, pk=pk)
            serializer = FincaDisableSerializer(finca, data=request.data, context={'request': request}, required=False)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {
                'error': False,
                'message': 'Finca actualizada correctamente'
            }
        except:
            dict_response = {
                'error': True,
                'error': serializer.errors
            }

        return Response(dict_response)

    @swagger_auto_schema(request_body=FincaSerializer)
    def update(self, request, pk=None):
        query_set = Finca.objects.all()
        finca = get_object_or_404(query_set, pk=pk)
        serializer = FincaSerializer(finca, data=request.data, context={'request': request})
        try:
            serializer.is_valid()
            serializer.save()
            dict_response = {
                'error': False,
                'message': 'Finca actualizada correctamente'
            }
        except:
            dict_response = {
                'error': True,
                'message': serializer.errors
            }

        return Response(dict_response)


class BultoViewSet(viewsets.ViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=BultoSerializer)
    def create(self, request):
        serializer = BultoSerializer(data=request.data, context={"request": request})
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            bulto_id = serializer.data['id']
            control_bulto_detalle_list = []

            for bulto_detalles in request.data['detalles_bulto']:
                bulto_detalles['bulto'] = bulto_id
                control_bulto_detalle_list.append(bulto_detalles)

            # print(control_bulto_detalle_list)
            serializerBultoDetail = BultoDetallesSerializer(data=control_bulto_detalle_list, many=True,
                                                            context={'request': request})
            serializerBultoDetail.is_valid()
            serializerBultoDetail.save()
            dict_response = {"Error": False, "detail": "Bulto Guardado Correctamente"}

        except IntegrityError as e:
            dict_response = {"Error": True, "detail": serializer.errors}

        return Response(dict_response)

    def list(self, request):
        bultos = ControlBultos.objects.filter(estado=True)
        serializer = BultoSerializer(bultos, many=True, context={"request": request})
        bultos_data = serializer.data
        bultos_list = []

        for bultos in bultos_data:
            bultos_detalle = ControlBultosDetalle.objects.filter(bulto=bultos["id"])
            bultos_detalle_serializer = BultoDetallesSerializer(bultos_detalle, many=True)
            bultos["controlbultos_detalle"] = bultos_detalle_serializer.data
            bultos_list.append(bultos)

        response = {"error": False, "message": "Todos los datos de bultos", "data": bultos_list}
        return Response(response)

    @swagger_auto_schema(request_body=DisableBultoSerializer)
    @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', url_name="Disable Bulto",
            name="Disable Bulto")
    def disable_bulto(self, request, pk=None):
        query_set = ControlBultos.objects.all()
        bulto = get_object_or_404(query_set, pk=pk)
        serializer = DisableBultoSerializer(bulto, data=request.data, context={'request': request}, required=False)
        try:

            serializer.is_valid()
            serializer.save()
            response = {
                'error': False,
                'message': 'Bulto deshabilitado correctamente'
            }

        except:
            response = {
                'error': True,
                'message': serializer.errors
            }

        return Response(response)


class BultoDetallesViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=BultoDetallesSerializer)
    def create(self, request):
        control_bulto_detalle_list = []

        try:
            for bulto_detalles in request.data['detalles_bulto']:
                control_bulto_detalle_list.append(bulto_detalles)

            serializerBultoDetail = BultoDetallesSerializer(data=control_bulto_detalle_list, many=True,
                                                            context={'request': request})
            serializerBultoDetail.is_valid(raise_exception=True)
            serializerBultoDetail.save()
            response = {
                'Error': False,
                'Message': 'Detalles guardado correctamente'
            }
        except:
            response = {
                'Error': True,
                'Message': serializerBultoDetail.errors
            }
        return Response(response)

    # @swagger_auto_schema(request_body=BultoDetallesDeleteSerializer)
    # @action(detail=True, methods=['delete'], url_path=r'delete/(?P<pk>\w+)', name='Delete Bulto Detail')
    def destroy(self, request, pk=None):
        query_set = ControlBultosDetalle.objects.all()
        detalles = get_object_or_404(query_set, pk=pk)

        # serializer = BultoDetallesDeleteSerializer(detalles)
        # serializer.is_valid()
        try:
            detalles.delete()
            dict_response = {
                'error': False,
                'message': 'Detalle borrado correctamente'
            }
        except:
            dict_response = {
                'error': True,
                'message': 'serializer.errors'
            }

        return Response(dict_response)


class PilonViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=PilonSerializer)
    def create(self, request):
        serializer = PilonSerializer(data=request.data, context={'request': request})
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'detail': 'Pilon Guardado Correctamente'}

        except IntegrityError as e:
            response = {'Error': True, 'detail': serializer.errors}

        return Response(response)

    def list(self, request):
        pilones = Pilon.objects.filter(estado=True)
        serializer = PilonSerializer(pilones, many=True, context={'request': request})
        response = {
            'Error': False,
            'message': 'Todos los pilones',
            'data': serializer.data
        }

        return Response(response)

    @swagger_auto_schema(request_body=PilonDisableSerializer)
    @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', url_name="Disable Pilon",
            name="Disable an Pilon")
    def disable_pilon(self, request, pk=None):
        try:
            queryset = Pilon.objects.all()
            pilon = get_object_or_404(queryset, pk=pk)
            serializer = PilonDisableSerializer(pilon, data=request.data, context={'request': request}, required=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Pilon deshabilitado correctamente'}

        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)

    @swagger_auto_schema(request_body=PilonSerializer)
    def update(self, request, pk=None):
        try:
            queryset = Pilon.objects.all()
            pilon = get_object_or_404(queryset, pk=pk)
            serializer = PilonSerializer(pilon, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Pilon Actualizado Correctamente'}

        except:
            response = {
                'Error': True,
                'message': serializer.errors
            }

        return Response(response)


class ClaseViewSet(viewsets.ViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=ClaseSerializer)
    def create(self, request):
        serializer = ClaseSerializer(data=request.data, context={'request': request})
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Clase Guardada Correctamente'}
        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)

    def list(self, request):
        clases = Clase.objects.filter(estado=True)
        serializer = ClaseSerializer(clases, many=True, context={'request': request})
        response = {
            'Error': False,
            'message': 'Todos las Clases',
            'data': serializer.data
        }
        return Response(response)

    @swagger_auto_schema(request_body=DisableClaseSerializer)
    @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', url_name='Disable Clase',
            name='Disable Clase')
    def disable_clase(self, request, pk=None):
        try:
            queryset = Clase.objects.all()
            clases = get_object_or_404(queryset, pk=pk)
            serializer = DisableClaseSerializer(clases, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Guardado Correctamente'}
        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)

    @swagger_auto_schema(request_body=ClaseSerializer)
    def update(self, request, pk=None):
        try:
            queryset = Clase.objects.all()
            clases = get_object_or_404(queryset, pk=pk)
            serializer = ClaseSerializer(clases, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Clase Actualizada correctamente'}
        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)


class CorteViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=CorteSerializer)
    def create(self, request):
        serializer = CorteSerializer(data=request.data, context={'request': request})
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {
                'Error': False,
                'Message': 'Corte guardado correctamente'
            }

        except:
            response = {
                'Error': True,
                'message': serializer.errors
            }

        return Response(response)

    def list(self, request):
        cortes = Corte.objects.filter(estado=True)
        serializer = CorteSerializer(cortes, many=True, context={'request': request})
        response = {
            'Error': False,
            'message': 'Lista de cortes',
            'data': serializer.data
        }

        return Response(response)

    @swagger_auto_schema(request_body=DisableCorteSerializer)
    @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', name='Disable Corte')
    def disable_corte(self, request, pk=None):
        try:
            queryset = Corte.objects.all()
            cortes = get_object_or_404(queryset, pk=pk)
            serializer = DisableCorteSerializer(cortes, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Corte desactivado correctamente'}

        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)

    @swagger_auto_schema(request_body=CorteSerializer)
    def update(self, request, pk=None):
        try:
            queryset = Corte.objects.all()
            cortes = get_object_or_404(queryset, pk=pk)
            serializer = CorteSerializer(cortes, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Corte Actualizado correctamente'}
        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)


class VariedadViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=VariedadSerializer)
    def create(self, request):
        serializer = VariedadSerializer(data=request.data, context={'request': request})
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Variedad Creada correctamente'}

        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)

    def list(self, request):
        variedades = Variedad.objects.filter(estado=True)
        serializer = VariedadSerializer(variedades, many=True, context={'request': request})
        response = {
            'Error': False,
            'message': 'Lista de Variedades',
            'data': serializer.data
        }

        return Response(response)

    @swagger_auto_schema(request_body=DisableVariedadSerializer)
    @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', name='Disable Variedad')
    def disable_variedad(self, request, pk=None):
        try:
            queryset = Variedad.objects.all()
            variedad = get_object_or_404(queryset, pk=pk)
            serializer = DisableVariedadSerializer(variedad, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Variedad desactivada correctamente'}

        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)

    @swagger_auto_schema(request_body=VariedadSerializer)
    def update(self, request, pk=None):
        try:
            queryset = Variedad.objects.all()
            variedades = get_object_or_404(queryset, pk=pk)
            serializer = VariedadSerializer(variedades, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Variedad guardad correctamente'}
        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)
    # En caso Si no pongo el detail=False no se muestra el id ni la url en swagger
    #
class TemperaturaBultoViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=TemperaturaBultoSerializer)
    def create(self, request):
        serializer = TemperaturaBultoSerializer(data=request.data, context={'request': request})
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Control de temperatura guardado'}

        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)

    def list(self, request):
        temperatura = ControlTemperaturaBultos.objects.filter(estado=True)
        serializer = TemperaturaBultoSerializer(temperatura, many=True, context={'request': request})
        response = {
            'Error': False,
            'message': 'Pilones con temperatura',
            'data': serializer.data
        }

        return Response(response)

    @swagger_auto_schema(request_body=DisableTemperaturaSerializer)
    @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', name='Disable Temperatura')
    def disable_control_temperatura_pilon(self, request, pk=None):
        try:
            queryset = ControlTemperaturaBultos.objects.all()
            temperatura = get_object_or_404(queryset, pk=pk)
            serializer = DisableTemperaturaSerializer(temperatura, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Pilon Temperatura desactivado correctamente'}

        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)

    @swagger_auto_schema(request_body=DisableTemperaturaSerializer)
    def update(self, request, pk=None):
        try:
            queryset = ControlTemperaturaBultos.objects.all()
            temperatura = get_object_or_404(queryset, pk=pk)
            serializer = VariedadSerializer(temperatura, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {'Error': False, 'message': 'Pilon Tempertaura actualizado correctamente'}
        except:
            response = {'Error': True, 'message': serializer.errors}

        return Response(response)
    # En caso Si no pongo el detail=False no se muestra el id ni la url en swagger
# En este caso para evitar eso,  si se deja en detail=True la url la muestra area/{id}/disabled que
# esta al reves y debe de ser /areas/disabled/{id}, entonces se pone en detail=False y se le pasa el parametro
# url_path que sobreescribira la url por una nueva como se puede probar en el swagger

# @swagger_auto_schema(request_body=DisableBultoSerializer)
# @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', url_name="Disable Bulto",
#        name="Disable an DisableBulto")
