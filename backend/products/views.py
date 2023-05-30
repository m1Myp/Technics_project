from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.settings import EMAIL_HOST_USER
from parsers.parse_catalogs import parse_catalogs
from parsers.parse_one_product import parse_one_product
from products.models import Categories, Info, URL, Pictures, Cost
from rest_framework import viewsets, generics

from .settings import BUG_REPORT_EMAILS
from .tools.pagination import get_page
from .tools.products_sort import sort_products
from .tools.work_with_db import clean_db, load_one_product
from .serializers import Product_serializer
from django.db.models import F, Func, Min, OrderBy, Q
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("(╯ ° □ °) ╯ (┻━┻).............. <br>")


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
    parse_catalogs()
    return HttpResponse("(╯ ° □ °) ╯ (┻━┻).............. <br>")


def clean(request):
    clean_db()
    return HttpResponse("База почищена")


class ProductList(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = Product_serializer


@api_view(['GET'])
def view_product_by_id(request, product_id):
    product_id = int(product_id)
    product = Info.objects.filter(product_ID=product_id).first()
    availability = {}
    for url in product.urls.all():
        availability[url.product_URL] = parse_one_product(url.product_URL)['availability']

    serializer = Product_serializer(product, many=False)
    data = serializer.data
    urls = data['urls']
    while True:
        flag = False
        for i in range(len(urls) - 1):
            if urls[i]['cost']['product_cost'] > urls[i + 1]['cost']['product_cost']:
                flag = True
                urls[i], urls[i + 1] = urls[i + 1], urls[i]
        if not flag:
            break
    for i in range(len(urls)):
        urls[i]['availability'] = availability[urls[i]['product_URL']]
    return Response(data)


def view_default(request, category):
    return view_with_filter(request, category, 0)


def view_with_filter(request, category, page):
    return view_with_filter_and_sort(request, category, page, 'min_price_asc')


@api_view(['GET'])
def view_with_filter_and_sort(request, category, page, sorting_type):
    category_id = Categories.objects.get(category_name=category).category_ID
    all_products = Info \
        .objects \
        .filter(product_category_ID=category_id)
    all_products = sort_products(all_products, sorting_type)
    products = get_page(all_products, page)
    serializer = Product_serializer(products, many=True)
    products_data = serializer.data
    for i in range(len(products_data)):
        urls = products_data[i]['urls']
        if len(urls) == 0:
            continue
        while True:
            flag = False
            for j in range(len(urls) - 1):
                if urls[j]['cost']['product_cost'] > urls[j + 1]['cost']['product_cost']:
                    flag = True
                    urls[j], urls[j + 1] = urls[j + 1], urls[j]
            if not flag:
                break
        products_data[i]['urls'] = urls
    data = {'products': products_data, 'total_count_products': len(all_products.all())}
    return Response(data)


def view_with_search(request, search_query):
    return view_with_search_page_sort(request, search_query, 0, 'min_price_asc')


@api_view(['GET'])
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
    products_data = serializer.data
    for i in range(len(products_data)):
        urls = products_data[i]['urls']
        if len(urls) == 0:
            continue
        while True:
            flag = False
            for j in range(len(urls) - 1):
                if urls[j]['cost']['product_cost'] > urls[j + 1]['cost']['product_cost']:
                    flag = True
                    urls[j], urls[j + 1] = urls[j + 1], urls[j]
            if not flag:
                break
        products_data[i]['urls'] = urls
    data = {'search_query': search_query, 'products': products_data, 'total_count_products': len(all_products.all())}
    return Response(data)
