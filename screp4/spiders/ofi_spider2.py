import scrapy
from bs4 import BeautifulSoup
from screp4.items import Screp4Item


class OfiSpider2(scrapy.Spider):

    name = "ofi2"
    allowed_domains = ["https://www.ofi-am.fr/produit"]
    start_urls = [
        "https://www.ofi-am.fr/produit"
    ]

    def parse(self, response):
        # data in the table
        #print(response.text)
        soup = BeautifulSoup(response.body)
        for url in soup.find_all('h6'):
            urlNext = url.contents[0].get('href')
            #print(urlNext)
            yield scrapy.Request(urlNext, callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        item = Screp4Item()
        soup = BeautifulSoup(response.body)
        fundName = soup.find('h1').string
        isin = soup.find('div', class_='code_isin').find('span').string
        item['fundName'] = fundName
        item['ISIN'] = isin
        yield item
        #télécharger les pdf
        urlProspectus = soup.find('div', class_='download-docs').find_all('a')[2].get(
            'href')
        yield scrapy.Request(urlProspectus, callback=self.save_pdf, dont_filter=True)

    def save_pdf(self,response):
        path1 = response.url.split('/')[-1]
        path = 'data/ofi/'+path1
        self.logger.info('Saving PDF %s', path)
        with open(path, 'wb') as f:
            f.write(response.body)







