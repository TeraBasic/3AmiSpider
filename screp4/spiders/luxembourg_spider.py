import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import csv
import json
from screp4.items import Screp4Item
class HermesSpider(scrapy.Spider):
    name = "luxembourg"

    allowed_domains = ["www.banquedeluxembourg.com/fr/bank/"]

    start_urls = [
        "https://www.banquedeluxembourg.com/fr/bank/corporate/bli_donnees-fonds-et-fiches-techniques"
    ]

    def parse(self, response):
        # data in the table
        #print(response.text)
        sel = Selector(response)
        trs = sel.xpath('//tr')
        for tr in trs:
            item = Screp4Item()
            name = tr.xpath('td[1]/a/text()').extract()
            currency = tr.xpath('td[3]/text()').extract()
            if (name!=" " and currency!=" "):
                item['shareName'] = name
                item['currency'] = currency
                yield item







