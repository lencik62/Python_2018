# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotebotItem(scrapy.Item):
    # define the fields for your item here like:
    Quote = scrapy.Field()
    Author = scrapy.Field()
    Tags = scrapy.Field()
