import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import csv
import json
from screp4.items import Screp4Item


class GuinnessSpider(scrapy.Spider):

    name = "guinness"
    allowed_domains = ["https://www.guinnessfunds.com/"]
    start_urls = [
        "https://www.guinnessfunds.com/global-equity-income-fund/"
        "https://www.guinnessfunds.com/european-equity-income-fund/"
        "https://www.guinnessfunds.com/asian-equity-income-fund/"
        "https://www.guinnessfunds.com/emerging-markets-equity-income-fund/"
    ]

    def parse(self, response):
        # data in the table
        #print(response.text)
        sel = Selector(response)
        table = sel.xpath('//table[@class="gf_sharec"]/tbody')
        #print(table)
        trISIN = table.xpath('tr[9]')
        trBloomberg = table.xpath('tr[10]')
        trRate = table.xpath('tr[2]')
        tds = trRate.xpath('//th')
        #print(trISIN,trBloomberg)
        tdsIsin = trISIN.xpath('td')
        for td in tdsIsin :
            item = Screp4Item()
            isin = td.xpath('text()').extract()
            item['ISIN']=isin
            yield item

        tdsBloomberg = trBloomberg.xpath('td')
        for td in tdsBloomberg:
            item = Screp4Item()
            bloomberg_code = td.xpath('text()').extract()
            item['bloomberg_code'] = bloomberg_code
            yield item










