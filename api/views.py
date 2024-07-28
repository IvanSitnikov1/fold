from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import ApiUser, Fold, Product, Take
from api.permission import IsProvider, IsConsumer
from api.serializers import UserSerialiser, FoldSerializer, ProductSerializer, TakeSerializer
from api.tasks import add_product, send_info_add_product


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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsProvider()]

    def create(self, request, *args, **kwargs):
        """Добавление нового продукта и отправка уведомления"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        add_product.delay(serializer.data['name'], serializer.data['fold'])
        send_info_add_product.delay(
            request.user.email,
            serializer.validated_data['name'],
            serializer.validated_data['fold'].name,
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TakeModelViewSet(viewsets.ModelViewSet):
    """Создаются точки GRUD операций для бронирования продуктов"""
    permission_classes = [IsConsumer]
    queryset = Take.objects.all()
    serializer_class = TakeSerializer

    def get_queryset(self):
        return Take.objects.filter(user=self.request.user)
