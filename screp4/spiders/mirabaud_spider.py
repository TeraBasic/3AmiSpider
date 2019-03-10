import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import csv
import json
from screp4.items import Screp4Item


class MirabaudSpider(scrapy.Spider):

    name = "mirabaud"
    allowed_domains = ["https://www.mirabaud-am.com/en/funds/"]
    start_urls = [
        "https://www.mirabaud-am.com/en/funds/qual/funds-list/"
    ]

    def parse(self, response):
        # data in the table
        #print(response.text)
        sel = Selector(response)
        tds = sel.xpath('//tr')
        print(tds)
        for td in tds:
            sharename=td.xpath('a/text()').extract()
            print(sharename)








