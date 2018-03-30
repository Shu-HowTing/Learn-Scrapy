# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem

class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['douban.com']
    base_url = "https://movie.douban.com/top250?start="
    off_set = 0
    start_urls = [base_url+str(off_set)]

    def parse(self, response):
        node_list = response.xpath("//ol/li")
        #node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
  
        for node in node_list:
            # 构建item对象，用来保存数据
            item = DoubanItem()
            # 提取每个职位的信息
            #print(node)
            #print("*"*40)
            item['title'] = node.xpath(".//span[1]/text()").extract()[0]

            item['director'] = node.xpath(".//p/text()").extract()[0].split()[1]
            span = node.xpath(".//p[@class='quote']/span")
            if span is None:
                item['introduce'] = '########'
            else:
                item['introduce'] = span.xpath(".//text()").extract()[0]
            

            item['link'] = node.xpath(".//a[1]/@href").extract()[0]

            # yield 的重要性，是返回数据后还能回来接着执行代码
            yield item

        # 第一种写法：拼接url，适用场景：页面没有可以点击的请求连接，必须通过拼接url才能获取响应
        if self.off_set < 250:
            self.off_set += 25
            url = self.base_url + str(self.off_set)
            yield scrapy.Request(url, callback = self.parse)