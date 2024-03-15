from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ApiUser(AbstractUser):
    """Переопределенная модель пользователя"""
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    user_type = models.CharField(max_length=10)


class Fold(models.Model):
    """Модель склада"""
    name = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=120)
    fold = models.ForeignKey(
        Fold,
        related_name='products',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.fold.name}. Product: {self.name}'


class Take(models.Model):
    """Модель бронирования"""
    product = models.ForeignKey(
        Product,
        related_name='taken',
        unique=True,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        ApiUser,
        related_name='taken',
        on_delete=models.CASCADE
    )
