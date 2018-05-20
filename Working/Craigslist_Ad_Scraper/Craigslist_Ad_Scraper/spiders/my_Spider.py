import scrapy



class MySpider(scrapy.Spider):
    name = "job_hunter"
    start_urls = ["https://washingtondc.craigslist.org/d/jobs/search/jjj"] 

    # def __init__(self, name, URL):
    #     self.name = name
    #     self.URL = URL

    def parse(self, response):
        for title in response.xpath("//*[@id=\"sortable-results\"]/ul/li/p"):
            yield {"title" : title.xpath("a/text()").extract_first()}itle" : title.xpath("a/text()").extract_first()}