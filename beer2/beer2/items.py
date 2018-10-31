# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Beer2Item(scrapy.Item):
   total = scrapy.Field()
   aroma_score = scrapy.Field()
   appearance = scrapy.Field()
   flavor_score = scrapy.Field()
   mouthfeel = scrapy.Field()
   style = scrapy.Field()
   abv = scrapy.Field()
   ibu = scrapy.Field()
   brewer_description = scrapy.Field()
   aroma_description = scrapy.Field()
   flavor_description = scrapy.Field()
   overall_description = scrapy.Field()
   image = scrapy.Field()
   name = scrapy.Field()
   brewer = scrapy.Field()
