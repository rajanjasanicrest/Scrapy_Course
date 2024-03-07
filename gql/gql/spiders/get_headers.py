import scrapy


class GetHeadersSpider(scrapy.Spider):
    name = "get_headers"
    allowed_domains = ["www.apollographql.com"]
    start_urls = ["https://www.apollographql.com/blog/complete-api-guide"]

    def parse(self, response):
        headers_2 = response.xpath("//h2")
        headers_3 = response.xpath("//h3")

        for header_2 in headers_2:
            yield{
                "header_2_" : header_2.xpath("text()").get()
            }
        
        for header_3 in headers_3:
            yield{
                "header_3_" : header_3.xpath("text()").get() or header_3.xpath("strong/text()").get()
            }