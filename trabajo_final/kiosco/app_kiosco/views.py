from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoModelSerializer


class ProductoViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoModelSerializer
