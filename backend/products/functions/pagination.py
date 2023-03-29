PRODUCTS_ON_PAGE = 7


def get_page(all_products, page):
    return all_products.all()[PRODUCTS_ON_PAGE * page:PRODUCTS_ON_PAGE * (page + 1)]
