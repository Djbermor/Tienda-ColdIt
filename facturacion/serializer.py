from facturacion.models import Producto, Factura, Item #se importa las clases 
from rest_framework import serializers #se importa el framework rest 

# se cran las clases serializer, paquete de rest  

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo', 'valor', 'nombre']

class ItemSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    class Meta:
        model = Item
        fields = ['producto', 'cantidad', 'valor_total']

class FacturaSerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many=True)
    class Meta:
        model = Factura
        fields = ['cliente', 'valor_total', 'item_set']
