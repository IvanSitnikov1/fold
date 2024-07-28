from time import sleep
from datetime import datetime

from django.core.mail import send_mail

from fold.celery import app
from api.models import Product, Fold, ApiUser, Take


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


@app.task
def write_to_logs():
    """Запись в файл информации о забронированных товарах"""

    consumers = ApiUser.objects.filter(user_type='consumer')
    for user in consumers:
        taken = Take.objects.filter(user_id=user.pk)
        reversed_products = Product.objects.filter(taken__in=taken)
        for product in reversed_products:
            data = f'{datetime.now()} - {user.username} - {product.name}\n--- --- ---'
            with open('logs.txt', 'a') as f:
                print(data, file=f)
                print('--- --- ---', file=f)
