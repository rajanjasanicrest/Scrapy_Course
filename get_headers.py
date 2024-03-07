import scrapy


class GetHeadersSpider(scrapy.Spider):
    name = "get_headers"
    allowed_domains = ["www.apollographql.com"]
    start_urls = ["https://www.apollographql.com/blog/complete-api-guide"]

    def parse(self, response):
        pass
