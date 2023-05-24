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
                       product_manufacturer=product_data["manufacturer"]
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


def clean_db():
    Categories.objects.all().delete()


def update_product_cost(product_data):
    cost = product_data['cost']
    url = URL.objects.filter(product_URL=product_data['url']).first()
    cost_object = Cost.objects.filter(URL_ID=url)
    cost_object.product_cost = cost
    cost_object.save()



# def delete_product_by_url(product_url):
#     url = URL.objects.filter(product_URL=product_url)
#     Info.objects.filter(product_url=url)
