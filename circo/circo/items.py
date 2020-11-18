# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CircoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #Encabezado del artículo
    encabezado=scrapy.Field()

    #Resumen del artículo
    sumary=scrapy.Field()
    pass
