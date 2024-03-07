# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from . import pymongo

import logging

class MongodbPipeline:
    collection_name = "best_movies"

    
    def open_spider(self,spider):
        self.client = pymongo.MongoClient("mongodb+srv://rajanj:bdbbZgctC0jSP1bi@cluster0.rdgwsdh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client["IMDB"]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
