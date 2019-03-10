import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import csv
import json
from screp4.items import Screp4Item


class FirstTrustSpider(scrapy.Spider):

    name = "firsttrust"
    allowed_domains = ["www.ftportfolios.com/Retail/"]
    start_urls = [
        "https://www.ftportfolios.com/Retail/cef/ceflist.aspx"
    ]

    def parse(self, response):
        # data in the table
        #print(response.text)
        sel = Selector(response)
        trs = sel.xpath('//tr[@class="dataRow"]')
        for tr in trs:
            item = Screp4Item()
            tikerSympol = tr.xpath('td[1]/a/text()').extract()
            fundType = tr.xpath('td[2]/text()').extract()
            print(tikerSympol)
            print(fundType)
            item['shareName'] = tikerSympol
            item['currency'] = fundType
            yield item







