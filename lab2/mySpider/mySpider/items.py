# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    序号 = scrapy.Field()
    课程名称 = scrapy.Field()
    课程难度 = scrapy.Field()
    作业多少 = scrapy.Field()
    给分好坏 = scrapy.Field()
    收获大小 = scrapy.Field()
    选课类别 = scrapy.Field()
    教学类型 = scrapy.Field()
    课程类别 = scrapy.Field()
    开课单位 = scrapy.Field()
    课程层次 = scrapy.Field()
    学分 = scrapy.Field()
    
