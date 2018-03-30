# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):

    #职位
    position = scrapy.Field()
    #职位链接
    positionLink = scrapy.Field()
    #职位种类
    positionType = scrapy.Field()
    #人数
    positionNumber = scrapy.Field()
    #地点
    positionLocation = scrapy.Field()
    #发布日期
    publishTime = scrapy.Field()

    #pass
