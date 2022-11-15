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


class URL(models.Model):
    URL_ID = models.AutoField(primary_key=True)
    product_ID = models.ForeignKey(
        Info,
        on_delete=models.CASCADE
    )
    product_URL = models.TextField()
    product_shop = models.CharField(max_length=100)


class Pictures(models.Model):
    picture_ID = models.AutoField(primary_key=True)
    picture_URL = models.TextField()
    product_ID = models.ForeignKey(
        Info,
        on_delete=models.CASCADE
    )


class Cost(models.Model):
    product_ID = models.OneToOneField(
        Info,
        on_delete=models.CASCADE
    )
    product_cost = models.IntegerField()
    last_update = models.TimeField()
