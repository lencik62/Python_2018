# -*- coding: utf-8 -*-
import os
import glob
from scrapy import Spider
from scrapy.http import Request
from multiPageScrapper.items import MultipagescrapperItem

def product_info(response, value):
    return response.xpath('//th[text()="' + value + '"]/following-sibling::td/text()').extract_first()

class Spiook (Spider):
    name = 'bookSpy'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toScrape.com']


    # def __init__(self, category):
    #     self.start_urls = [category] 

    def parse (self, response):
        books = response.xpath("//h3/a/@href").extract()

        for book in books:
            absolute_url = response.urljoin(book)

            yield Request(absolute_url, callback= self.parse_book)

        next_page_url = response.xpath('//a[text() = "next"]/@href').extract_first()
        absolute_next_page_url =  response.urljoin(next_page_url)
        yield  Request(absolute_next_page_url, callback= self.parse)


    def parse_book(self, response):
        title =  response.xpath("//h1/text()").extract()
        price =  response.xpath('//*[@class = "price_color"]/text()').extract_first()
        image_url =  response.xpath('//img/@src').extract_first()
        image_url =  image_url.replace('../../','http://books.toScrape.com/')
        rating =  response.xpath('//*[contains(@class, "star-rating")]/@class').extract_first()
        rating = rating.replace('star-rating',"")
        description = response.xpath('//*[@id = "product_description"]/following-sibling::p/text()').extract_first()
        description = description.replace('...more','...')

        # product information data points
        upc = product_info(response, 'UPC')
        product_type =  product_info(response, 'Product Type')
        price_without_tax = product_info(response, 'Price (excl. tax)')
        price_with_tax = product_info(response, 'Price (incl. tax)')
        tax = product_info(response, 'Tax')
        availability = product_info(response, 'Availability')
        number_of_reviews = product_info(response, 'Number of reviews')

        items = MultipagescrapperItem()

        items['title'] = title
        items['price'] = price
        items['image_url'] = image_url
        items['rating'] = rating
        items['description'] = description
        items['details'] = {
            "upc" : upc,
            "product_type" : product_type,
            "price_without_tax" : price_without_tax,
            "price_with_tax" : price_with_tax,
            "tax" : tax,
            "availability" : availability,
            "number_of_reviews" : number_of_reviews,
            }
        yield items

    # def close(self, reason):
    #     csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
    #     os.rename(csv_file, 'foobar.csv')