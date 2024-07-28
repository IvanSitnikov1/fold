# API для склада

---

#### Описание  
Учебный проект - API для склада.  
Реализовано 2 типа пользователей: поставщик и потребитель. Поставщик имеет возможность добавлять товары на склады, но не может бронировать товары. Потребитель же наоборот - может только бронировать товары.  
Есть возможность просмотреть товары, оставщиеся на конкретном складе.  
Потребитель может отдельно увидеть товары, которые он забронировал.  

К проекту добавлена очередь задач celery с базой данных redis. При добавлении продукта асинхронно отправляется письмо на почту поставщика. Само добавление в БД занимает 10с (имитация какой-то проверки товара).  
Так же во время работы приложения каждые 5 мин в файл logs.txt записывается информация вида - 'дата и время - пользователь - его забронированные товары'.

#### Конечные точки API  
POST: http://127.0.0.1:8000/users/ - создание пользователя  
GET: http://127.0.0.1:8000/users/ - получение пользователей  
GET: http://127.0.0.1:8000/users/{pk}/ - получение конкретного пользователя  
PUT: http://127.0.0.1:8000/users/{pk}/ - редактирование информации он пользователе  

POST: http://127.0.0.1:8000/folds/ - создание склада  
GET: http://127.0.0.1:8000/folds/ - получение складов  
GET: http://127.0.0.1:8000/folds/{pk}/ - получение конкретного склада  
PUT: http://127.0.0.1:8000/folds/{pk}/ - редактирование информации о склада  
DELETE: http://127.0.0.1:8000/folds/{pk}/ - удаление склада  
GET: http://127.0.0.1:8000/folds/{pk}/products/ - получение продуктов, имеющихся на складе  

POST: http://127.0.0.1:8000/products/ - добавление продукта на склад (только для поставщика)  
GET: http://127.0.0.1:8000/products/ - получение продуктов  
GET: http://127.0.0.1:8000/products/{pk}/ - получение конкретного продукта  
PUT: http://127.0.0.1:8000/products/{pk}/ - редактирование продукта (только для поставщика)  
DELETE: http://127.0.0.1:8000/products/{pk}/ - удаление продукта (только для поставщика)  

Доступно только для потребителя:  
POST: http://127.0.0.1:8000/takes/ - бронирование продукта со склада(каждый продукт можно забронировать только один раз)  
GET: http://127.0.0.1:8000/takes/ - получение забронированных продуктов  
GET: http://127.0.0.1:8000/takes/{pk}/ - получение конкретного продукта  
PUT: http://127.0.0.1:8000/takes/{pk}/ - редактирование продукта  
DELETE: http://127.0.0.1:8000/takes/{pk}/ - удаление продукта  

#### Запуск проекта: python manage.py runserver
Приложение запускается по адресу: http://127.0.0.1:8000/  

*Данные для тестирования:  
Поставщик:  
Логин: provider  
Пароль: 12332113  
Потребитель:  
Логин: consumer  
Пароль: 12332113*  
Приложение наполнил минимальными данными, необходимыми для тестирования функционала  
