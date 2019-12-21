# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#   This file holds storage "containers" for the data we want to scrape

import scrapy


# class StackOverflowItem(scrapy.Item):
#     pass


from scrapy import Item, Field


class StackOverflowItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    url = Field()
