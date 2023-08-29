from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.models import ApiUser, Fold, Product, Take
from api.permission import IsProvider, IsConsumer
from api.serializers import UserSerialiser, FoldSerializer, ProductSerializer, TakeSerializer

# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'path', 'get']
    serializer_class = UserSerialiser


class FoldModelViewSet(viewsets.ModelViewSet):
    queryset = Fold.objects.all()
    serializer_class = FoldSerializer

    @action(detail=True)
    def products(self, request, pk=None):
        fold = get_object_or_404(Fold.objects.all(), id=pk)
        free_products = fold.products.filter(taken__isnull=True)
        return Response(
            ProductSerializer(free_products, many=True).data
        )


class ProductModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsProvider]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TakeModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsConsumer]
    queryset = Take.objects.all()
    serializer_class = TakeSerializer