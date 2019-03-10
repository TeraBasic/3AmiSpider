import scrapy
from scrapy.selector import Selector
from screp4.items import Screp4Item


class OfiSpider(scrapy.Spider):

    name = "ofi"
    allowed_domains = ["https://www.ofi-am.fr/produit"]
    start_urls = [
        "https://www.ofi-am.fr/produit"
    ]

    def parse(self, response):
        # data in the table
        #print(response.text)
        sel = Selector(response)
        funds = sel.xpath('//h6')
        #print(tds)
        for fund in funds:
            item = Screp4Item()
            fundName=fund.xpath('a/text()').extract()
            isin=fund.xpath('span/text()').extract()
            item['fundName'] = fundName
            item['ISIN'] = isin
            yield item









