import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import csv
import json
from screp4.items import Screp4Item


class BellevueSpider(scrapy.Spider):

    name = "bellevue"

    allowed_domains = ["https://www.bellevue.ch/en/asset-management/"]

    start_urls = [
        "https://www.bellevue.ch/en/asset-management/products-performance/"
    ]

    def parse(self, response):
        # data in the table
        # print(response.text)
        sel = Selector(response)
        trs = sel.xpath('//div[@class="products"]')
        print(trs)
        for td in trs:
            print(td)
            # item = Screp4Item()
            # name = td.xpath('p/text()').extract()
            # print(name)
