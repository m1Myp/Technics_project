import scrapy
from scrapy.crawler import CrawlerProcess


def normalize_int(y):
    return list(map(lambda x: x.translate({ord('\n'): None, ord(' '): None}), y))


def normalize_str(y):
    return list(map(lambda x: " ".join(x.split()), y))


class MySpider(scrapy.Spider):
    name = 'citilink_manufacturers_spider'
    start_urls = ['https://www.citilink.ru/brands/']
    custom_settings = {
        'LOG_ENABLED': False,
    }

    def parse(self, response, **kwargs):
        print(len(response.css("li.BrandBook__column-item a.Link_type_default::text")))
        for brand in response.css("li.BrandBook__column-item a.Link_type_default::text"):
            yield {
                "name": brand.get()
            }


if __name__ == '__main__':
    items = open("spiders/manufacturers.json", "w")
    items.close()

    process = CrawlerProcess(settings={
        "FEED_FORMAT": "json",
        "FEED_URI": "spiders/manufacturers.json",
        "FEED_EXPORT_ENCODING": "utf-8",
        "ROBOTSTXT_OBEY": False,
    })

    process.crawl(MySpider)
    process.start()  # the script will block here until the crawling is finished
