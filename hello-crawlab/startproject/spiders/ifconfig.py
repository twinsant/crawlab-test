import scrapy


class IfconfigSpider(scrapy.Spider):
    name = 'ifconfig'
    allowed_domains = ['https://ifconfig.io/']
    start_urls = ['http://https://ifconfig.io//']

    def parse(self, response):
        pass
