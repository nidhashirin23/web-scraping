import scrapy


class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["w3school.com"]
    start_urls = ["https://w3school.com"]

    def parse(self, response):
        pass
