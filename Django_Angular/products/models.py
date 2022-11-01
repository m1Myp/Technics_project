from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    manufacturer = models.TextField(default='none')
    picture = models.TextField(default='')

    def __str__(self):
        return self.name
