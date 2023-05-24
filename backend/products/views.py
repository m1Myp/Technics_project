import json
import os
from subprocess import Popen, PIPE
import subprocess

from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail

from backend.settings import EMAIL_HOST_USER
from products.models import Categories, Info, URL, Pictures, Cost
from rest_framework import viewsets, generics

from .settings import BUG_REPORT_EMAILS
from .tools.pagination import get_page
from .tools.products_sort import sort_products
from .tools.work_with_db import clean_db, load_one_product
from .serializers import Product_serializer


def index(request):
    return HttpResponse("(╯ ° □ °) ╯ (┻━┻).............. <br>")


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def bug_report(request):
    if request.method == "POST":
        print(request.POST)
        send_mail(
            "Bug report from technics nearby project",
            "user mail:" + request.POST['email'] + "\nbug report message:" + request.POST['bug_report_message'],
            EMAIL_HOST_USER,
            BUG_REPORT_EMAILS,
        )
    return HttpResponse("(╯ ° □ °) ╯ (┻━┻).............. <br>")


def scrap_all(request):
    data = []
    names = ""

    for i in data:
        load_one_product(i)

        names += i["name"] + "<br>"
    return HttpResponse("БАЗИРУЕМСЯ.............. <br>" + names)


def clean(request):
    clean_db()
    return HttpResponse("База почищена")


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


from django.db.models import F, Func, Min, OrderBy, Q


def view_default(request, category):
    return view_with_filter(request, category, 0)


def view_with_filter(request, category, page):
    return view_with_filter_and_sort(request, category, page, 'min_price_asc')


def view_with_filter_and_sort(request, category, page, sorting_type):
    category_id = Categories.objects.get(category_name=category).category_ID
    all_products = Info \
        .objects \
        .filter(product_category_ID=category_id)
    all_products = sort_products(all_products, sorting_type)
    products = get_page(all_products, page)
    serializer = Product_serializer(products, many=True)
    data = {'products': serializer.data, 'total_count_products': len(all_products.all())}
    return JsonResponse(data, safe=False)


def view_with_search(request, search_query):
    return view_with_search_page_sort(request, search_query, 0, 'min_price_asc')


def view_with_search_page_sort(request, search_query, page, sorting_type):
    all_products = Info \
        .objects \
        .filter(Q(product_name__icontains=search_query) |
                Q(product_category_ID__category_name__icontains=search_query) |
                Q(product_manufacturer__icontains=search_query)
                )
    all_products = sort_products(all_products, sorting_type)
    products = get_page(all_products, page)
    serializer = Product_serializer(products, many=True)
    data = {'search_query': search_query, 'products': serializer.data, 'total_count_products': len(all_products.all())}
    return JsonResponse(data, safe=False)
