import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor 
from circo.items import CircoItem
from scrapy.exceptions import CloseSpider

class CircoSpider(CrawlSpider):
    name='article'
    item_count=0 #esto nos ayudará a limitar la cantidad de items a scrapear
    allowed_domain=['https://elcomercio.pe/']
    start_urls=['https://elcomercio.pe/politica/', 
    'https://elcomercio.pe/ultimas-noticias/',
    'https://elcomercio.pe/economia/']

    rules={
        Rule(LinkExtractor(allow =(), restrict_xpaths=('//div[@class="story-item__btn flex justify-center mt-20 uppercase"]/a'))),
        
    }