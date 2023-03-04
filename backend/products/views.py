import json
import os
from subprocess import Popen, PIPE
import subprocess

from django.http import HttpResponse, JsonResponse

from products.models import Categories, Info, URL, Pictures, Cost
from rest_framework import viewsets, generics
from .serializers import Product_serializer


def index(request):
    cmd = ['venv/Scripts/python', 'spiders/citilink_manufacturers.py']
    process = subprocess.Popen(cmd, env=os.environ, stdout=PIPE, stderr=PIPE)
    process.wait()

    cmd = ['venv/Scripts/python', 'spiders/citilink_all_script.py']
    process = subprocess.Popen(cmd, env=os.environ)
    process.wait()

    # f = open("all.json", encoding='utf-8')
    data = json.load(process.stdout)
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

        cost = Cost(URL_ID=urlI,
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


# class ProductsViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Info.objects.all()
#     serializer_class = Product_serializer

class ProductList(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = Product_serializer


# class ProductDetail(generics.RetrieveAPIView):
#     queryset = Info.objects.all()
#     serializer_class = Product_serializer


def view_product_by_id(request, product_id):
    product_id = int(product_id)
    products = Info.objects.filter(product_ID=product_id).first()
    serializer = Product_serializer(products, many=False)

    return JsonResponse(serializer.data, safe=False)


PRODUCTS_ON_PAGE = 7


def view_with_filter(request, category, page=0):
    category_ID = Categories.objects.get(category_name=category).category_ID
    all_products = Info.objects.filter(product_category_ID=category_ID)
    products = all_products.all()[
               PRODUCTS_ON_PAGE * page:PRODUCTS_ON_PAGE * (page + 1)]
    serializer = Product_serializer(products, many=True)
    data = {'products': serializer.data, 'total_count_products': len(all_products.all())}
    return JsonResponse(data, safe=False)
