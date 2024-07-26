from time import sleep

from django.core.mail import send_mail

from fold.celery import app
from api.models import Product, Fold


@app.task
def add_product(name, fold_pk):
    """Добавление тавара в базу данных"""
    # имитация каких-то проверок при добавлении товара
    sleep(10)

    fold = Fold.objects.get(pk=fold_pk)
    Product.objects.create(name=name, fold=fold)

@app.task
def send_info_add_product(email, product, fold):
    """Отправка уведомления на email о добавлении товара"""
    send_mail(
        'Продукт',
        f'Продукт "{product}" добавлен на склад "{fold}"',
        'contrheil@gmail.com',
        [email],
        fail_silently=False,
    )
