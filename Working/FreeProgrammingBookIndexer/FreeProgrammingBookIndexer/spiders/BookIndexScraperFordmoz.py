import scrapy


class BookIndexScraperFordmoz(scrapy.Spider):
    name = "dmoz-indexer"
    start_urls =  ['http://dmoz-odp.org/Computers/Programming/Languages/Python/Books/']

    def parse(self,response):

        for listing in response.xpath('//*[@id="site-list-content"]/div/div/a'):
            if(listing.xpath('div/text()').extract_first() is not None):
                yield {
                "Index" : listing.xpath('div/text()').extract_first(),
                "url"   : listing.xpath('@href').extract_first()
            }