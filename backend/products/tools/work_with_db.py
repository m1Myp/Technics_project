from comparator.comparator import compare
from products.models import Categories, Info, URL, Pictures, Cost


def load_one_product(product_data):
    # Create category
    if not (Categories.objects.filter(category_name=product_data["category"])):
        c = Categories(category_name=product_data["category"])
        c.save()

    # Find category in model
    category = Categories.objects.filter(category_name=product_data["category"]).first()

    # Create Product Info for this product and save it
    product = Info.objects.filter(product_name=product_data['name']).first()
    if not product:
        product = Info(product_category_ID=category,
                       product_name=product_data["name"],
                       product_manufacturer=product_data["manufacturer"],
                       product_characteristics=product_data['characteristics']
                       )
        product.save()

    # Save all pictures in db
    for pict in product_data["pictures"]:
        picture = Pictures(picture_URL=pict, product_ID=product)
        picture.save()

    # Save url in db
    url = URL(product_ID=product,
              product_URL=product_data["url"],
              product_shop=product_data["shop"]
              )
    url.save()

    # Save cost in db
    cost = Cost(URL_ID=url,
                product_cost=product_data["cost"],
                )
    cost.save()


def load_many_products(products_data):
    if len(products_data) == 0:
        return
    category = Categories.objects.filter(category_name=products_data[0]["category"]).first()
    products_names = list(map(lambda x: x['name'], products_data))
    names_in_db = list(map(lambda x: x.product_name, Info.objects.filter(product_category_ID=category).all()))
    new_names = compare(names_in_db, products_names)
    for i in range(len(products_data)):
        if new_names[i] == '':
            continue
        products_data[i]['name'] = new_names[i]
    for product in products_data:
        load_one_product(product)


def clean_db():
    Categories.objects.all().delete()


def update_product_cost(product_data):
    cost = product_data['cost']
    url = URL.objects.filter(product_URL=product_data['url']).first()
    cost_object = Cost.objects.filter(URL_ID=url).first()
    cost_object.product_cost = cost
    cost_object.save()
