# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HaofsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    num = scrapy.Field()
    salary = scrapy.Field()
    nature = scrapy.Field()
    update_time = scrapy.Field()
    info = scrapy.Field()
    pass
