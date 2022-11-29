import scrapy
from scrapy.crawler import CrawlerProcess


def normalize_int(y):
    return list(map(lambda x: x.translate({ord('\n'): None, ord(' '): None}), y))


def normalize_str(y):
    return list(map(lambda x: " ".join(x.split()), y))


class MySpider(scrapy.Spider):
    name = 'citilink_spider'

    def parse(self, response, **kwargs):
        product_name = response.css("h1::text").extract()
        product_name = normalize_str(product_name)[0]
        # print(product_name)

        product_cost = response.css("span.ProductPagePriceSection__default-price_current-price::text").extract()
        product_cost = normalize_int(product_cost)
        if len(product_cost) == 0:
            product_cost = response.css("span.ProductHeader__price-default_current-price::text").extract()
            product_cost = normalize_int(product_cost)
        product_cost = product_cost[0]

        print(product_cost)
        yield {"name": product_name,
               "cost": product_cost}


if __name__ == '__main__':
    urlfile = open("url.txt")
    url = urlfile.read()
    urlfile.close()


    class AnotherSpider(MySpider):
        start_urls = [url]


    items = open("items.json", "w")
    items.close()

    process = CrawlerProcess(settings={
        "FEED_FORMAT": "json",
        "FEED_URI": "items.json",
        "FEED_EXPORT_ENCODING": "utf-8",
        "ROBOTSTXT_OBEY": False,
    })

    process.crawl(AnotherSpider)
    process.start()  # the script will block here until the crawling is finished
