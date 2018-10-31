# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    brewer = scrapy.Field()
    beer_type = scrapy.Field()
    release = scrapy.Field()
    state = scrapy.Field()
    description = scrapy.Field()
    abv = scrapy.Field()
    ibu = scrapy.Field()
    serv_temp = scrapy.Field()
    hops = scrapy.Field()
    malts = scrapy.Field()
    aroma = scrapy.Field()
    appearance = scrapy.Field()
    flavor = scrapy.Field()
    mouthfeel = scrapy.Field()
    overall_impression = scrapy.Field()
    brewer_intro = scrapy.Field()
    review = scrapy.Field()



