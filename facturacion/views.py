from django.shortcuts import render
from rest_framework.response import Response
from facturacion.models import Producto, Factura, Item
from facturacion.serializer import ProductoSerializer, FacturaSerializer
from rest_framework import viewsets, status

#View o vista de Producto
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#View o vista de Factura
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    #Funcion create, la cual genera los totales de la factura y item
    def create(self, request):
        factura = Factura.objects.create(cliente=request.data.get('cliente', 'Na'), valor_total=0)
        valor_total_factura = 0
        for item in request.data['item_set']:
            valor_total = item['cantidad'] * item['producto']['valor']
            producto = Producto.objects.get(codigo=item['producto']['codigo'])
            Item.objects.create(valor_total=valor_total, producto=producto, cantidad=item['cantidad'],
                                factura=factura)
            valor_total_factura += valor_total

        factura.valor_total = valor_total_factura
        factura.save()
        return Response({}, status=status.HTTP_201_CREATED)