# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Screp4Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fundName = scrapy.Field()
    shareName = scrapy.Field()
    ISIN = scrapy.Field()
    shareClass = scrapy.Field()
    currency = scrapy.Field()
    unitType = scrapy.Field()
    assetClass = scrapy.Field()
    bloomberg_code = scrapy.Field()
    pass
