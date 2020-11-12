# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:59:11 2020
Baseado no projeto de LEONARDO KUFFO

"""


from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
#from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class Articulo(Item):
    titulo = Field()
    description = Field()     
    sales = Field()
    reference = Field()
    item_image = Field()
    price = Field()
    
 #'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36',
 #'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadoLibre'
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',    
        #'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36',
        #'CLOSESPIDER_PAGECOUNT': 3 # Numero maximo de paginas que buscara itens. Scrapy termina quando atinge esse limite
        'CLOSESPIDER_ITEMCOUNT': 30 # Numero maximo de itens 
    }

    #  domínios permitidos, pois os artigos usam um domínio diferente em cada pagina
    allowed_domains = ['produto.mercadolivre.com.br', 'lista.mercadolivre.com.br', 'mercadolivre.com.br']

    start_urls = ['https://lista.mercadolivre.com.br/iphone-x#D[A:iphone%20x]'] # cole o link da busca do mercado livre aqui

    download_delay = 2

    # Tupla de regras
    rules = (            
        Rule( # REGRA #1 => HORIZONTALIDADE POR PÁGINA
            LinkExtractor(
                allow=r'/_Desde_\d+' # Padrão onde é usado "\d+", expressão que pode assumir o valor de qualquer combinação de números
            ), follow=True),
        Rule( # REGRA #2 => VERTICALIDADE AO DETALHE DOS PRODUTOS
            LinkExtractor(
                allow=r'/MLB-' 
            ), follow=True, callback='parse_items'), # Ao inserir o detalhe dos produtos, o callback é chamado com a resposta ao pedido
    )

    def parse_items(self, response):

        item = ItemLoader(Articulo(), response)     

        
        # Uso do Map Compose com funções anônimas
        item.add_xpath('titulo', '//h1/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        item.add_xpath('description', '//p[@class="ui-pdp-description__content"]/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
		
        item.add_xpath('sales', '//div[@class="ui-pdp-header__subtitle"]/span/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        item.add_value('reference', response.url)
        item.add_value('item_image', response.css('.ui-pdp-gallery__figure img::attr(data-src)').extract())


        

        soup = BeautifulSoup(response.body)
        price = soup.find(class_="price-tag")
        price_completo = price.text.replace('\n', ' ').replace('\r', ' ').replace(' ', '')
        item.add_value('price', price_completo)



        yield item.load_item()