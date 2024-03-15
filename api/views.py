from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import ApiUser, Fold, Product, Take
from api.permission import IsProvider, IsConsumer
from api.serializers import UserSerialiser, FoldSerializer, ProductSerializer, TakeSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    """Создаются точки создания, получения и изменения пользователя"""
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'put', 'get']
    serializer_class = UserSerialiser


class FoldModelViewSet(viewsets.ModelViewSet):
    """Создаются точки GRUD операций над складами"""
    queryset = Fold.objects.all()
    serializer_class = FoldSerializer

    @action(detail=True)
    def products(self, request, pk=None):
        """Action получает информацию по продуктам, оставшимся на складе"""
        fold = get_object_or_404(Fold.objects.all(), id=pk)
        free_products = fold.products.filter(taken__isnull=True)
        return Response(
            ProductSerializer(free_products, many=True).data
        )


class ProductModelViewSet(viewsets.ModelViewSet):
    """Создаются точки GRUD операций над продуктами"""
    permission_classes = [IsProvider]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TakeModelViewSet(viewsets.ModelViewSet):
    """Создаются точки GRUD операций для бронирования продуктов"""
    permission_classes = [IsConsumer]
    queryset = Take.objects.all()
    serializer_class = TakeSerializer
