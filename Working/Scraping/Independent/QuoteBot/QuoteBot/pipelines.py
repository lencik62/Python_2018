# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QuotebotPipeline(object):
    def process_item(self, item, spider):
        if item['Author']:
            item['Author'] = [author.upper() for author in item['Author']]
        if item['Quote']:
            item['Quote'] = [  quote.replace('\u201c', "") for quote in item['Quote']]
            item['Quote'] = [  quote.replace('\u201d', "") for quote in item['Quote']]

        return item
