# Technics_project
[Схема базы данных](https://dbdesigner.page.link/Ym2u8tmLXPM5FgZG8)
### Что где лежит
В папке **djangoProject** лежит тестовый проект с Django.
В папке **Django_Angular** лежит тестовый проект объединяющий Django и Angular. Сделан на подобие [проекта](https://www.twilio.com/blog/build-progressive-web-application-django-angular-part-1-backend-api)
В папке **backend** лежат все текущие наработки по backend-у.
### backend
##### Нужные python packages
- scrapy
- django-cors-headers
- djangorestframework
- Django
- scrapy-splash
- возможно что то ещё
##### Запуск
2 варианта:
1. Открыть папку как PyCharm project и запустить.
2. Открыть командную строку и ввести
```
python manage.py runserver
```
##### Поведение
- по ссылке http://127.0.0.1:8000/admin/ можно зайти через (user: admin, password: 1234) и смотреть состояние БД и менять её
- перейдя по ссылке http://127.0.0.1:8000/products/ запуститься скрапер и выгрузит все продукты из каталогов указанных в файле spiders/categories_urls.json. После все загрузится в БД.
- перейдя по ссылке http://127.0.0.1:8000/products/scrap_all запуститься Скрапер(citilink_script.py) одного продукта из Ситилинка, который проскрапит ссылку, хранящуюся в файле url.txt и сохранит резеультаты в файл items.json. БД не как не меняется
- по ссылке http://127.0.0.1:8000/products/api/v1/test/ будет json file со всеми продуктами