from django.urls import path, include
from rest_framework.routers import DefaultRouter
from facturacion.views import ProductoViewSet, FacturaViewSet

router = DefaultRouter()
router.register(r'producto', ProductoViewSet)
router.register(r'factura', FacturaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]