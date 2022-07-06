# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['https://www.indeed.com']
    start_urls = ['http://https://www.indeed.com/']

    def parse(self, response):
        pass
