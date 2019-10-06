from django.db import models
from django.core.validators import MinValueValidator


class Producto(models.Model):
    nombre = models.CharField("Nombre Producto", max_length=50, blank=False, null=False)
    descripcion = models.TextField("Descripción", blank=False, null=True)
    codigo = models.CharField(max_length=100, unique=True)
    precio_sugerido = models.DecimalField("Precio sugerido de Venta", blank=False, null=False,
                                          validators=[MinValueValidator(1, message="El precio debe ser mayor a $0")],
                                          max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre
