#tutorial from http://newcoder.io/scrape/part-0/
import scrapy
from scrapy import Request
from craigslist.items import IndeedItem

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
#run "scrapy crawl jobs -o result-titles.csv" from console to save results to csv

class JobsSpider(scrapy.Spider):
    name = 'eicherList02'
    allowed_domains = ['https://www.indeed.com']
    start_urls = ['https://www.indeed.com/q-Police-Officer-l-Orlando,-FL-jobs.html']

    jobs_list_xpath = '//td[@id="resultsCol"]/div[@class="  row  result"]'
    item_fields = {
            'title': './/h2/a/text()',
            'absolute_url': './/h2/a/@href',
            'company': './/span/span/a/text()',
            'location': './/span[@itemprop="jobLocation"]/span/span/text()'
            }
    
#starting reference point for the tags in jobs loop
    def parse(self, response):
        #jobs = response.xpath('//td[@id="resultsCol"]/div[@class="  row  result"]')
        
        selector = HtmlXPathSelector(response)
        
        for job in selector.select(self.jobs_list_xpath):
            loader = XPathItemLoader(IndeedItem(), selector=job)
        # define processors
            loader.default_input_processor = MapCompose(str.strip)
            loader.default_output_processor = Join()
        
        # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
        
        


        relative_next_url = response.xpath('//td[@id="resultsCol"]/div/a[5]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
        print("!!!!TESTING!!!! " + relative_next_url)
        yield Request(absolute_next_url, callback=self.parse)
        
