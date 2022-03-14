from rest_framework.decorators import api_view, action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from drf_yasg.utils import swagger_auto_schema, swagger_serializer_method
from .serializer import AreaSerializer, AreaDisabledSerializer
from .models import Area



# This two classes allow me to add the user name to the token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['area_id'] = user.area_id
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#@permission_classes([IsAuthenticated])
class AreaView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=AreaSerializer)
    def create(self, request):
        serializer = AreaSerializer(data=request.data, context={"request": request})
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"Error": False, "detail": "Area Guardada Correctamente"}
        except:
            dict_response = {"Error": True, "detail": serializer.errors}

        return Response(dict_response)

    def list(self, request):

        area = Area.objects.filter(estado=True)
        # area = Area.objects.all()
        serializer = AreaSerializer(area, many=True, context={'request': request})
        response_dic = {
            'error': False,
            'message': 'Todas las areas',
            'data': serializer.data
        }
        return Response(response_dic)

    # En caso Si no pongo el detail=False no se muestra el id ni la url en swagger
    # En este caso para evitar eso,  si se deja en detail=True la url la muestra area/{id}/disabled que
    # esta al reves y debe de ser /areas/disabled/{id}, entonces se pone en detail=False y se le pasa el parametro
    # url_path que sobreescribira la url por una nueva como se puede probar en el swagger
    @swagger_auto_schema(request_body=AreaDisabledSerializer)
    @action(detail=False, methods=['patch'], url_path=r'disable/(?P<pk>\w+)', url_name="Disable Area",
            name="Disable an Area")
    def disable_area(self, request, pk=None):

        try:
            query_set = Area.objects.all()
            area = get_object_or_404(query_set, pk=pk)
            serializer = AreaDisabledSerializer(area, data=request.data, context={'request': request}, required=False)
            serializer.is_valid()
            serializer.save()
            dic_response = {
                'error': False,
                'message': 'Area deshabilitada correctamente'
            }
        except:
            dic_response = {
                'error': True,
                'message': serializer.errors
            }
        return Response(dic_response)

    @swagger_auto_schema(request_body=AreaSerializer)
    def update(self, request, pk=None):
        # query_set = Area.objects.all()
        # area = get_object_or_404(query_set, pk=pk)
        # serializer = AreaSerializer(area, data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     response = {
        #         'error': False,
        #         'message': 'Actualizado Correctamente'
        #     }
        # else:
        #
        #     response = {
        #         'error': True,
        #         'message': serializer.errors
        #     }
        try:
            query_set = Area.objects.all()
            area = get_object_or_404(query_set, pk=pk)
            serializer = AreaSerializer(area, data=request.data, context={'request': request})
            serializer.is_valid()
            serializer.save()
            response = {
                'error': False,
                'message': 'Area deshabilitada correctamente'
            }
        except :
            response = {
                'error': True,
                'message': serializer.errors
            }
        return Response(response)
