# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CodeSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    s_id = scrapy.Field()
    save_code = scrapy.Field()
    pass
