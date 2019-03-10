import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import csv


class HermesSpider(scrapy.Spider):
    name = "hermes1"

    def __init__(self):
        #self.driver = webdriver.Chrome('/usr/local/bin/')
        self.driver = webdriver.Safari()

    allowed_domains = ["www.hermes-investment.com"]

    start_urls = [
        "https://www.hermes-investment.com/fr/products/"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #print(response.text)
        self.driver.get(response.url)
        # Output filename
        # Selector for all the names from the link with class 'ng-binding'
        filename = "angular_data.csv"
        elements = self.driver.find_elements_by_css_selector("content")
        print(elements)
        print("i am here")
        print('')
    '''
    def parse(self, response):
        print("I am here")
        sel = Selector(response)
        trs = sel.xpath('//tr')
        for tr in trs:
            fundName = tr.xpath('td[1]/text()').extract()
            ISIN = tr.xpath('td[9]/text()').extract()
            shareClass = tr.xpath('td[2]/text()').extract()
            currency = tr.xpath('td[5]/text()').extract()
            unitType = tr.xpath('td[3]/text()').extract()
            assetClass = tr.xpath('td[4]/text()').extract()
            print("I am here")
            print(fundName, ISIN, shareClass, currency, unitType, assetClass)

        
        for trbody in response.xpath('//tr'):
            print("I am here")
            for tr in trbody.xpath('tr'):
                fundName = tr.xpath('td[1]/text()').extract()
                ISIN = tr.xpath('td[9]/text()').extract()
                shareClass = tr.xpath('td[2]/text()').extract()
                currency = tr.xpath('td[5]/text()').extract()
                unitType = tr.xpath('td[3]/text()').extract()
                assetClass = tr.xpath('td[4]/text()').extract()
                print ("I am here")
                print (fundName, ISIN, shareClass, currency, unitType, assetClass)
        '''




