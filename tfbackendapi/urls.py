
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (

    TokenRefreshView,
)

from authentication.views import MyTokenObtainPairView
from curacion import views
from authentication.views import AreaView


schema_view = get_schema_view(
    openapi.Info(
        title="Tabacos Fran API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="pabelandino@gmail.com"),
        license=openapi.License(name="License de uso"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register("finca", views.FincaViewSet, basename='Finca')
router.register("bultos", views.BultoViewSet, basename='Bultos')
router.register("areas", AreaView, basename='Area')
router.register("clase", views.ClaseViewSet, basename='Clase')
router.register("corte", views.CorteViewSet, basename='Corte')
router.register("variedad", views.VariedadViewSet, basename='Variedad')
router.register("pilones", views.PilonViewSet, basename='Pilon')
router.register("bulto_detalles", views.BultoDetallesViewSet, basename='Bulto Detalles')
router.register("bulto_temperatura", views.TemperaturaBultoViewSet, basename='Bulto Detalles Temperatura')
#router.register("areas/disabled/<str:pk>/", AreaView.as_view({'get':'disable_area'}), basename='AreaDisable')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]


