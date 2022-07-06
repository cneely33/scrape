#tutorial from http://python.gotrained.com/scrapy-tutorial-web-scraping-craigslist/
import scrapy
from scrapy import Request
from scraper_app.items import IndeedItem

#from scrapy.selector import HtmlXPathSelector
#from scrapy.contrib.loader import XPathItemLoader
#from scrapy.contrib.loader.processor import Join, MapCompose
#run "scrapy crawl jobs -o result-titles.csv" from console to save results to csv

class JobsSpider(scrapy.Spider):
    name = 'eicherList01'
    allowed_domains = ['https://www.indeed.com']
    start_urls = ['https://www.indeed.com/q-Police-Officer-l-Orlando,-FL-jobs.html']

#starting reference point for the tags in jobs loop
    def parse(self, response):
        jobs = response.xpath('//td[@id="resultsCol"]/div[@class="  row  result"]')
        
        for job in jobs:
            
            title0 = job.xpath('h2/a/text()').extract_first()
            title1 = job.xpath('h2/a/b/text()').extract_first()
            title = title0 + ("" + title1 if title1 else "")
            company = job.xpath('span/span/a/text()').extract_first()
            location = job.xpath('span[@itemprop="jobLocation"]/span/span/text()').extract_first("")
            relative_url = job.xpath('h2/a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
    
            yield{'URL':absolute_url, 'Title':title, 'Location':location, 'Company':company}


        relative_next_url = response.xpath('//td[@id="resultsCol"]/div/a[5]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
        print("!!!!TESTING!!!! " + relative_next_url)
        yield Request(absolute_next_url, callback=self.parse)
        
