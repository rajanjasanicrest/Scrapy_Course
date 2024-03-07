# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class BookstoscrapeItem(scrapy.Item):
    image_url = scrapy.Field()
    images = scrapy.Field()
    book_name = scrapy.Field(
        output_processor = TakeFirst()
    )