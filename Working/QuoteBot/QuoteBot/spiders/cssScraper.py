from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from QuoteBot.items import QuotebotItem


class cssScraper(Spider):
    name = "cssSpider"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ["http://quotes.toscrape.com"]

    # for x in range(1, 10, 1):
    #     start_urls.append("http://quotes.toscrape.com/page/{}/".format(x))

    def parse(self, response):

        quotes = response.xpath(
            "/html/body/div/div/div/div/span[1]/text()").extract()
        tags_s = response.xpath('/html/body/div/div/div/div/div/meta/@content').extract()
        authors = response.xpath(
            "/html/body/div/div/div/div/span/small/text()").extract()
        for quote, tags, author in zip(quotes, tags_s, authors):
            item = ItemLoader(item=QuotebotItem(), response=response)
            item.add_value('Quote', quote)
            item.add_value('Author', author)
            item.add_value('Tags', tags)

            yield item.load_item()
        next_page_url = response.xpath(
            '//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)
