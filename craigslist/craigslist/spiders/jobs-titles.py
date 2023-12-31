# -*- coding: utf-8 -*-
import scrapy
#run "scrapy crawl jobs -o result-titles.csv" from console to save results to csv

class JobsSpider(scrapy.Spider):
    name = 'jobs-titles'
    allowed_domains = ['https://orlando.craigslist.org/search/sec']
    start_urls = ['https://orlando.craigslist.org/search/sec']

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        for title in titles:
            yield {'Title': title}

