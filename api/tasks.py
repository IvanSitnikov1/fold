from django.core.mail import send_mail

from fold.celery import app


@app.task
def send_info_add_product(email, product, fold):
    send_mail(
        'Продукт',
        f'Продукт "{product}" добавлен на склад "{fold}"',
        'contrheil@gmail.com',
        [email],
        fail_silently=False,
    )
