import scrapy


class ImageSpiderPySpider(scrapy.Spider):
    name = "image_spider.py"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
