# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    TimeLimit = scrapy.Field()
    MemoryLimit = scrapy.Field()
    TotalSubmissions = scrapy.Field()
    Accepted = scrapy.Field()
    Description = scrapy.Field()
    Input = scrapy.Field()
    OutPut = scrapy.Field()
    SampleInput = scrapy.Field()
    SampleOutput = scrapy.Field()
    Hint = scrapy.Field()
    Source = scrapy.Field()
