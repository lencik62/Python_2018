# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from time import sleep
from selenium.common.exceptions import  NoSuchElementException
from BookGrabber.items import BookgrabberItem
class sel_spider_multi_page(Spider):
    name = 'sel'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = driver = webdriver.Chrome("chromedriver")
        self.driver.get("http://books.toscrape.com/")
        
        sel = Selector(text = self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:
            url = "http://books.toscrape.com/" + book

            yield Request (url , callback = self.parse_book)
        while True:
            try:
                self.driver.find_element_by_xpath('//a[text() ="next"]').click()
                sleep(3)
                self.logger.info('Sleeping for 3 seconds')
                sel = Selector(text = self.driver.page_source)
                books = sel.xpath('//h3/a/@href').extract()
                for book in books:
                    url = "http://books.toscrape.com/catalogue/" + book

                    yield Request (url , callback = self.parse_book)
            except NoSuchElementException:
                self.logger.info("No more pages to load")

                break

    def parse_book(self, response):
        items = BookgrabberItem()
        title = response.css('h1::text').extract_first()
        url = response.request.url
    
        items['title'] = title
        items['url'] = url
        yield items