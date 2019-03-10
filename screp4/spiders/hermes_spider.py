import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import csv
import json
from screp4.items import Screp4Item
class HermesSpider(scrapy.Spider):
    name = "hermes"

    allowed_domains = ["www.hermes-investment.com"]

    start_urls = [
        "https://cdn-api.kurtosys.io/tools/ksys319/fundfinder/getfundfinder?country=France&lang=French&maxresults=500&searchbyquerystring=%7B%22Fund+Status+Taxonomy%22:%5B%22Seeded%22%5D,%22Registered+Country+Id%22:%5B%22France%22%5D%7D&startfrom=0"

    ]

    def parse(self, response):
        # data in the table
        json_data = json.loads(response.text)
        list = json_data['data']
        # list = json_data['name']['Fund Size Currency Code']['Asset Class Taxonomy Id']['Units']
        fundList = list['fundList']
        for fund in fundList:
            for share in fund['children']:
                item=Screp4Item()
                item['shareName']=share['name']
                item['ISIN'] = share['identifiers']['ISIN Code']
                item['unitType'] = share['properties']['Units']
                item['currency'] = share['properties']['Price Currency Id']
                item['assetClass'] = share['properties']['Asset Class Taxonomy Id']
                item['shareClass'] = share['properties']['Shareclass Category Taxonomy Id']
                #print(name, ISIN, Units, currency, asset_class, share_class, end='')
                yield item
                print('')





