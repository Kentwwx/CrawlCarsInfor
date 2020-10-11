# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestcrawlItem(scrapy.Item):
    title = scrapy.Field()
    car = scrapy.Field()
    reply = scrapy.Field()