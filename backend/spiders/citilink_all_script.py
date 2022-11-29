import scrapy, json
from scrapy.crawler import CrawlerProcess


def normalize_int(y):
    return list(map(lambda x: x.translate({ord('\n'): None, ord(' '): None}), y))


def normalize_str(y):
    return list(map(lambda x: " ".join(x.split()), y))


urlsFile = open("spiders/categories_urls.json", encoding='utf-8')
categories_urls = json.load(urlsFile)
urls = [categories_urls[i]['citilink_url'] for i in categories_urls]
urlsFile.close()


class MySpider(scrapy.Spider):
    name = 'citilink_all_spider'
    start_urls = urls
    custom_settings = {
        # 'LOG_ENABLED': False,
    }

    def parse(self, response, **kwargs):
        product_category = ""
        for i in categories_urls:
            if i in response.url.split('/'):
                product_category = i
                break

        for product in response.css('div.ProductCardVerticalLayout'):
            if len(product.css('span.ProductCardVerticalPrice__price-current_current-price::text').extract()) == 0:
                continue
            product_name = product.css('a.ProductCardVertical__name').attrib['title']

            product_manuf = ""
            for manufacturer in manufacturers:
                if product_name.find(manufacturer['name']) != -1 :
                    product_manuf = manufacturer['name']
                    break

            product_cost = normalize_int(
                    product
                    .css('span.ProductCardVerticalPrice__price-current_current-price::text')
                    .extract())[0]

            product_url = 'https://www.citilink.ru' \
                          + product.css('a.ProductCardVertical__name').attrib['href']

            product_picture = product.css('img.ProductCardVertical__picture').attrib['src']

            yield {
                'name': product_name,
                'manufacturer': product_manuf,
                'cost': product_cost,
                'category': product_category,
                'url': product_url,
                'shop': 'citilink',
                'pictures': [product_picture],
            }
        next_page_url = response.css('a.PaginationWidget__arrow_right')
        if len(next_page_url) != 0:
            yield scrapy.Request(response.urljoin(next_page_url.attrib['href']))


if __name__ == '__main__':
    items = open("all.json", "w")
    items.close()

    manufacturers_file = open("spiders/manufacturers.json", encoding='utf-8')
    manufacturers = json.load(manufacturers_file)
    manufacturers_file.close()

    process = CrawlerProcess(settings={
        "FEED_FORMAT": "json",
        "FEED_URI": "all.json",
        "FEED_EXPORT_ENCODING": "utf-8",
        "ROBOTSTXT_OBEY": False,
        "COOKIES_ENABLED": False,
        "DOWNLOAD_DELAY": '2',
        "DOWNLOADER_MIDDLEWARES": {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        },
    })

    process.crawl(MySpider)
    process.start()  # the script will block here until the crawling is finished
