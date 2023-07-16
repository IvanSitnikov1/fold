from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ApiUser(AbstractUser):
    ...


class Fold(models.Model):
    name = models.CharField(max_length=120)


class Product(models.Model):
    name = models.CharField(max_length=120)
    fold = models.ForeignKey(Fold, related_name='products', on_delete=models.CASCADE)


class Take(models.Model):
    product = models.ForeignKey(Product, related_name='taken', on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name='taken', on_delete=models.CASCADE)