from rest_framework import serializers

from .models import Producto


class ProductoModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'codigo',
            'precio',
        ]