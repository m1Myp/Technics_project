import json
import os
import subprocess

from django.http import HttpResponse

from products.models import Categories, Info, URL, Pictures, Cost


def index(request):
    cmd = ['venv/Scripts/python', 'spiders/citilink_manufacturers.py']
    process = subprocess.Popen(cmd, env=os.environ)
    process.wait()

    cmd = ['venv/Scripts/python', 'spiders/citilink_all_script.py']
    process = subprocess.Popen(cmd, env=os.environ)
    process.wait()

    f = open("all.json", encoding='utf-8')
    data = json.load(f)
    names = ""

    for i in data:
        if not (Categories.objects.filter(category_name=i["category"])):
            c = Categories(category_name=i["category"])
            c.save()

        c = Categories.objects.filter(category_name=i["category"]).first()

        if URL.objects.filter(product_URL=i["url"]):
            product = URL.objects.filter(product_URL=i["url"]).first().product_ID
            product.delete()

        product = Info(product_category_ID=c,
                       product_name=i["name"],
                       product_manufacturer=i["manufacturer"]
                       )
        product.save()

        for pict in i["pictures"]:
            picture = Pictures(picture_URL=pict, product_ID=product)
            picture.save()

        urlI = URL(product_ID=product,
                   product_URL=i["url"],
                   product_shop=i["shop"]
                   )
        urlI.save()

        cost = Cost(product_ID=product,
                    product_cost=i["cost"],
                    )
        cost.save()

        names += i["name"] + "<br>"
    return HttpResponse("БАЗИРУЕМСЯ.............. <br>" + names)


def scrap_all(request):
    cmd = ['venv/Scripts/python', 'spiders/citilink_script.py']
    process = subprocess.Popen(cmd, env=os.environ)
    process.wait()
    return HttpResponse("Скрапим.............. <br>")


from rest_framework import viewsets
from .serializers import Product_serializer


class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Info.objects.all()
    serializer_class = Product_serializer
