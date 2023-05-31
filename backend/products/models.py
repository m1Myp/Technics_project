from django.db import models


class Categories(models.Model):
    category_ID = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)


class Info(models.Model):
    product_ID = models.AutoField(primary_key=True)
    product_category_ID = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE
    )
    product_name = models.TextField()
    product_manufacturer = models.CharField(max_length=100)
    product_characteristics = models.TextField(
        default="Тип: внешний жесткий диск(жестче некуда), объем: 1ТБ(1ТБ = 2^43 бит), Интерфейсы подключения: USB 3.0, Формат: 2.5\"(A4), Цвет: Черный(как моя душа)")


class URL(models.Model):
    URL_ID = models.AutoField(primary_key=True)
    product_ID = models.ForeignKey(
        Info,
        related_name='urls',
        on_delete=models.CASCADE
    )
    product_URL = models.TextField()
    product_shop = models.CharField(max_length=100)


class Pictures(models.Model):
    picture_ID = models.AutoField(primary_key=True)
    picture_URL = models.TextField()
    product_ID = models.ForeignKey(
        Info,
        related_name='pictures',
        on_delete=models.CASCADE
    )


class Cost(models.Model):
    URL_ID = models.OneToOneField(
        URL,
        related_name='cost',
        on_delete=models.CASCADE
    )
    product_cost = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
