# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class BooksSpider(CrawlSpider):
    name = 'Books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (Rule(LinkExtractor(
        # no google links
        deny_domains=("google.com"),
        # only url with key word music
        # allow=("music")
        ), 
        callback='parse_page',
        # do you want to follow all the url in the page until no new url is found
        follow=True),)

    def parse_page(self, response):
        yield{"url": response.url}
