import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = "best_movies"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250   "]

    rules = ( Rule(LinkExtractor(restrict_xpaths='//div[@class="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg cli-title"]/a[@class="ipc-title-link-wrapper"]'), callback="parse_item", follow=True),  )

    def parse_item(self, response):
        yield {
            'title' : response.xpath('//div[@class="sc-69e49b85-0 jqlHBQ"]/h1/span/text()').get(),
            'year' : response.xpath('//div[@class="sc-69e49b85-0 jqlHBQ"]/ul/li[1]/a/text()').get(),
            'duration' : response.xpath('//div[@class="sc-69e49b85-0 jqlHBQ"]/ul/li[3]/text()').get(),
            'rating' : response.xpath('//div[@class="sc-69e49b85-0 jqlHBQ"]/ul/li[2]/a/text()').get(),
            'movie_url' : response.url  ,
        }