from django.db import models

#se crea las entidades 

#clase producto 
class Producto(models.Model):
	codigo = models.TextField(unique=True)
	valor = models.FloatField()
	nombre = models.TextField()
	def __str__(self):
		return f'{self.codigo}'

#clase factura
class Factura(models.Model):
	cliente = models.TextField()
	valor_total = models.FloatField()
	def __str__(self):
		return f'{self.id} cliente: {self.cliente}'

#clase Item
class Item(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad = models.FloatField()
	valor_total = models.FloatField()
	factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.id}'

