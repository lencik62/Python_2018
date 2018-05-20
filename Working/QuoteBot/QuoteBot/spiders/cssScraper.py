import scrapy

class cssScraper(scrapy.Spider):
    name = "cssSpider"
    start_urls = ["http://quotes.toscrape.com/"]
    for x in range(1, 10, 1):
        start_urls.append("http://quotes.toscrape.com/page/{}/".format(x))

    def parse(self, response):
        print(len(self.start_urls), self.start_urls[8])
        for quote in response.css("div.quote"):
            yield {
                "quote": quote.css("span.text::text").extract_first(),
                "author": quote.css("small.author::text").extract_first(),
                "tags": quote.css("div.tags > a.tag::text").extract()}
