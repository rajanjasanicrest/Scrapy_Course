import scrapy


class BestSellerGlassesSpider(scrapy.Spider):
    name = "best_seller_glasses"
    allowed_domains = ["www.glassesshop.com"]
    start_urls = ["https://www.glassesshop.com/bestsellers"]
        
    def parse(self, response):
        glasses = response.xpath('//div[@class="row pt-lg-5 product-list column-1"]/div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]')
        for glass in glasses:

            prod_url = glass.xpath('.//div[@class="product-img-outer"]/a/@href').get()

            img_link = glass.xpath('.//div[@class="product-img-outer"]/a/img[@class="lazy d-block w-100 product-img-default"]/@data-src').get()

            prod_name = glass.xpath('.//div[@class="p-title-block"]/div[@class="mt-3"]/div/div[@class="col-6 col-lg-6"]/div[@class="p-title"]/a/@title').get()

            prod_price = glass.xpath('.//div[@class="p-title-block"]/div[@class="mt-3"]/div/div[@class="col-6 col-lg-6"]/div[@class="p-price"]/div/span/text()').get()

            yield {
                'prod_url' : prod_url,
                'img_link' : img_link,
                'prod_name' : prod_name,
                'prod_price' : prod_price,
            }

        next_page = response.xpath('//ul[@class = "pagination"]/li/a[@rel="next"]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)