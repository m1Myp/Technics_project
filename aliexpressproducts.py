import scrapy
from scrapy.crawler import CrawlerProcess

class AliexpresswaresSpider(scrapy.Spider):
    name = 'wares'
    items = open("items.json", "w")
    items.close()
    def start_requests(self):
        yield scrapy.Request('http://aliexpress.ru/')
    
    def parse(self,response):
        for link in response.css('li.SnowCategoriesMenu_SnowCategoriesMenu__categoryItem__1xev4 a::attr(href)'):
            yield response.follow(link.get(), callback = self.parse_categories)

    def parse_categories(self,response):
        products = response.css('div.product-snippet_ProductSnippet__description__lido9p')
        for product in products:
            yield{
                'name': product.css('div.product-snippet_ProductSnippet__name__lido9p::text').get().strip(), 
                'price': product.css('div.snow-price_SnowPrice__mainM__18x8np::text').get().strip(),
            }
        
process = CrawlerProcess(settings = {
    "FEED_FORMAT": "json",
        "FEED_URI": "items.json",
        "FEED_EXPORT_ENCODING": "utf-8",
        "ROBOTSTXT_OBEY": False,
})
process.crawl(AliexpresswaresSpider)
process.start()