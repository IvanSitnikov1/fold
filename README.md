# API для модели склада

#### [Ссылка на приложение](https://ivansitnikov1.pythonanywhere.com)

Цель: Разработка API для приложения, которое позволяет поставщикам и потребителям взаимодействовать со складом.

---

Описание

API имеет 4 маршрута, поддерживающие POST и GET запросы.  
"users": "http://127.0.0.1:8000/users/",  
"folds": "http://127.0.0.1:8000/folds/",  
"products": "http://127.0.0.1:8000/products/",  
"takes": "http://127.0.0.1:8000/takes/"  

"users" - позволяет создать пользователя с выбором его типа и получить текущих пользователей.  
"folds" - позволяет создать новый склад и просмотреть имеющиеся.  
"products" - позволяет добавить продукт на склад, доступно только для поставщиков.  
"takes" - позволяет забронировать товар со склада, доступно только потребителю. Невозможно несколько раз забронировать один и тот же товар.  

*Тестовые пользователи:  
Поставщик:  
Логин: provider  
Пароль: 12332113  
Потребитель:  
Логин: consumer  
Пароль: 12332113*  

#### Стек: Python | DRF
