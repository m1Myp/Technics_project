from django.db.models import Min, F, Max


def sort_products(all_products, sorting_type):
    if sorting_type.startswith('min'):
        all_products = all_products.annotate(cost=Min('urls__cost__product_cost'))
    if sorting_type.startswith('max'):
        all_products = all_products.annotate(cost=Max('urls__cost__product_cost'))
    if sorting_type.endswith('asc'):
        return all_products.order_by(F('cost').asc())
    if sorting_type.endswith('desc'):
        return all_products.order_by(F('cost').desc())
    return all_products
