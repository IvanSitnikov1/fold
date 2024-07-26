from rest_framework import serializers, validators

from api.models import ApiUser, Fold, Product, Take


class UserSerialiser(serializers.Serializer):
    """Сериализатор для модели пользователя"""
    USER_TYPE = (
        ('provider', 'Поставщик'),
        ('consumer', 'Потребитель'),
    )
    username = serializers.CharField(
        max_length=120,
        validators=[validators.UniqueValidator(ApiUser.objects.all())]
    )
    email = serializers.EmailField(
        validators=[validators.UniqueValidator(ApiUser.objects.all())]
    )
    password = serializers.CharField(
        min_length=6,
        max_length=20,
        write_only=True
    )
    user_type = serializers.ChoiceField(
        choices=USER_TYPE,
        label='Тип пользователя'
    )

    def update(self, instance, validated_data):
        """Редактирование данных пользователя"""
        if email := validated_data.get('email'):
            instance.email = email
            instance.save(update_fields=['email'])
        if password := validated_data.get('password'):
            instance.set_password(password)
            instance.save(update_fields=['password'])
        return instance

    def create(self, validated_data):
        """Создание пользователя"""
        user = ApiUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            user_type=validated_data['user_type'],
        )

        user.set_password(validated_data['password'])
        user.save(update_fields=['password'])
        return user


class FoldSerializer(serializers.ModelSerializer):
    """Сериализатор модели склада"""
    class Meta:
        model = Fold
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели продукта"""
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class TakeSerializer(serializers.ModelSerializer):
    """Сериализатор модели бронирования товара"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Take
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}
