# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MultipagescrapperPipeline(object):
    def process_item(self, item, spider):
        if item['description']:
            item['description'] =  item['description'].replace('...more','...')
            return item
        if item['image_url']:
            item['image_url'] =  item['image_url'].replace('../../','http://books.toScrape.com/')
            return item
        if item['rating']:
            item['rating'] =  item['rating'].replace('star-rating',"")
            return item
