# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBeginItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class userData(scrapy.Item):
    name = scrapy.Field()
    email = scrapy.Field()
    walletAddress = scrapy.Field()

