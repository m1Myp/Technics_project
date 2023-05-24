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
- по ссылке http://127.0.0.1:8000/products/api/v1/product/<id> будет json file с продуктом product_id которого совпадает с id. 
Например: http://127.0.0.1:8000/products/api/v1/product/484 отобразится продукт с product_id 484.
- по ссылке api/v1/c=<slug:category>/p=<int:page> будет json file страницы под номером page (страницы нумеруются с 0) продуктов категории category.
Например: http://127.0.0.1:8000/products/api/v1/c=myshi/p=12
- по ссылке api/v1/c=<slug:category> будет json file первой страницы продуктов категории category.
Например: http://127.0.0.1:8000/products/api/v1/c=myshi
Запрос эквивалентен запросу http://127.0.0.1:8000/products/api/v1/c=myshi/p=0
- по ссылке api/v1/c=<slug:category>/p=<int:page> будет json file страницы под номером page (страницы нумеруются с 0) продуктов категории category.
Например: http://127.0.0.1:8000/products/api/v1/c=myshi/p=12
- по ссылке api/v1/c=<slug:category> будет json file первой страницы продуктов категории category.
Например: http://127.0.0.1:8000/products/api/v1/c=myshi
Запрос эквивалентен запросу http://127.0.0.1:8000/products/api/v1/c=myshi/p=0
- по ссылке api/v1/c=<slug:category>/p=<int:page>&sorting=<slug:sorting_type> будет страница продуктов категории category отсортированные по sorting_type
Например: http://127.0.0.1:8000/products/api/v1/c=myshi/p=0&sorting=min_price_asc  -- сортировка по возрастанию минимальной цены
http://127.0.0.1:8000/products/api/v1/c=myshi/p=0&sorting=min_price_desc -- сортировка по убыванию минимальной цены
http://127.0.0.1:8000/products/api/v1/c=myshi/p=0&sorting=max_price_asc  -- сортировка по возрастанию максимальной цены
http://127.0.0.1:8000/products/api/v1/c=myshi/p=0&sorting=max_price_desc -- сортировка по убыванию максимальной цены
- по api/v1/q=<str:search_query>/p=<int:page>&sorting=<slug:sorting_type> будет страница продуктов содержащих search_query в названии, производителе или названии категории category отсортированные по sorting_type
Например: http://127.0.0.1:8000/products/api/v1/q=%D0%9C%D1%8B%D1%88%D1%8C/p=2&sorting=max_price_desc
http://127.0.0.1:8000/products/api/v1/q=Logitech/p=2&sorting=max_price_desc
- Bug report. 
ВНИМАНИЕ: прежде чем использовать bug report в файле backend/backend/settings.py нужно заполнить EMAIL_HOST_PASSWORD. Его надо спросить у владельца почты EMAIL_HOST_USER. Для безопастности почты владельца, он не должен загружаться на github.
Пример запроса используя python:
```
r = requests.post("http://127.0.0.1:8000/products/bug_report", data={'email':'sophyal@mail.ru', 'bug_report_message':'cringe project'})
```
