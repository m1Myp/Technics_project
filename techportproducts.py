import scrapy
from scrapy.crawler import CrawlerProcess

class TechportwaresSpider(scrapy.Spider):
    items = open("techitems.json", "w")
    items.close()
    
    name = 'technowares'

    def start_requests(self):
        yield scrapy.Request('https://www.techport.ru/katalog/products/otdelnostojaschaja-bytovaja-tehnika')
    # it is too long to scrape an entire website, so we will scrape a single big category with it's subcategories
    #def parse(self,response):
    #    for link in response.css('div.tcp-directory-item__content a::attr(href)'):
    #        yield response.follow(link.get(), callback = self.parse_categories)

    def parse(self,response):
        for link in response.css('div.categories-block div.tcp-container a::attr(href)'):
            yield response.follow(link.get(), callback = self.parse_products)

    def parse_products(self,response):
        products = response.css('div.tcp-product-body__title')
        for product in products:
            yield {
                'brand':product.css('a::attr(data-gtm-brand)').get().strip(),
                'name':product.css('a::attr(data-gtm-name)').get().strip(),
                'price':product.css('a::attr(data-gtm-price)').get().strip(),
                'link':product.css('a::attr(href)').get().strip(),
            }




process = CrawlerProcess(settings = {
    "FEED_FORMAT": "json",
        "FEED_URI": "techitems.json",
        "FEED_EXPORT_ENCODING": "utf-8",
        "ROBOTSTXT_OBEY": False,
})
process.crawl(TechportwaresSpider)
process.start()