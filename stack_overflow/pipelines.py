# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import json
from scrapy import settings
from scrapy.exceptions import DropItem
import logging


# class StackOverflowPipeline(object):
#     def process_item(self, item, spider):
#         return item


class MongoDBPipeline(object):
    """This pipeline is used for writing items to a mongodb database"""
    collection_name = 'questions'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

        # print(settings['MONGODB_DB'])
        # connection = pymongo.MongoClient(
        # settings['MONGODB_SERVER'],
        # settings['MONGODB_PORT']
        #  )

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.db[self.collection_name].insert_one(dict(item))
            logging.debug("Question added to MongoDB database!")
        return item


class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.json', 'w')

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item