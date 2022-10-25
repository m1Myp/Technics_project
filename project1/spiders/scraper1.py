import scrapy

class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    start_urls = ['https://citilink-nsk.blizko.ru/tovary/k-16881837-planshety']

    def parse(self, response):
        for products in response.css('li.cpl-item.clearfix'):
            yield{
                'name': products.css('a.cpi-title.js-os-link').attrib['data-text'],
                'price': products.css('i.bp-price.fsn::text').get(),
                'link': products.css('a.cpi-title.js-os-link').attrib['href'],
            }
        next_page = response.css('a.pli-link-.js-navigate').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
            