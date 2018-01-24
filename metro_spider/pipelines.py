# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json

from .items import *
from .settings import MONGO_URI, MONGO_DATABASE

class BasePipeline(object):
    collection_name = ''

    def __init__(self):
        self.mongo_uri = MONGO_URI
        self.mongo_db = MONGO_DATABASE

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
    #     )
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
       pass


class CityPipline(BasePipeline):
    collection_name = 'city'

    def process_item(self, item, spider):
        if isinstance(item, CityItem):
            self.db[self.collection_name].update({'name':item['name']}, {'$set':dict(item)}, True)
        return item

class MetroPipeline(BasePipeline):
    collection_name = 'metro'

    def process_item(self, item, spider):
        if isinstance(item, MetroItem):
            self.db[self.collection_name].update({'name': item['name']}, {'$set': dict(item)}, True)
        return item

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item