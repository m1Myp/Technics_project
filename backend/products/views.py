from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from products.models import Categories, Info, URL, Pictures, Cost
import json


def index(request):
    f = open("scraper/all.json", encoding='utf-8')
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
                    last_update=datetime.now()
                    )
        cost.save()

        names += i["name"] + "<br>"
    return HttpResponse("БАЗИРУЕМСЯ.............. <br>" + names)
