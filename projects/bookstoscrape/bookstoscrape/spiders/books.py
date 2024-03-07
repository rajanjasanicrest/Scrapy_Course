import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpider(CrawlSpider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    rules = (
                Rule(LinkExtractor(restrict_xpaths='//section/div/ol/li/article/h3/a'), callback="parse_item", follow=True),
                Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]/a')), 
            )

    def parse_item(self, response):
        yield{
            'title' : response.xpath('//h1').get(),
            'price' : response.xpath('//p[@class="price_color"]/text()').get()
        }
        