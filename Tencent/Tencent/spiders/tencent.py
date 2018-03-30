# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    base_url = "http://hr.tencent.com/position.php?keywords=&tid=0&lid=2218&start="
    offside = 0
    start_urls = [base_url + str(offside)]
    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
        # 构建item对象，用来保存数据
            item = TencentItem()
            # 提取每个职位的信息，并且将提取出的Unicode字符串编码为UTF-8编码
            item['position'] = node.xpath("./td[1]/a/text()").extract()[0]

            item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0]

            if len(node.xpath("./td[2]/text()")):
                item['positionType'] = node.xpath("./td[2]/text()").extract()[0]
            else:
                item['positionType'] = "NULL"

            item['positionNumber'] = node.xpath("./td[3]/text()").extract()[0]

            item['positionLocation'] = node.xpath("./td[4]/text()").extract()[0]

            item['publishTime'] = node.xpath("./td[5]/text()").extract()[0]

            # yield 的重要性，是返回数据后还能回来接着执行代码
            yield item
        # 第一种写法：拼接url，适用场景：页面没有可以点击的请求连接，必须通过拼接url才能获取响应
        if self.offside < 30 :
            self.offside  += 10
            next_url = self.base_url + str(self.offside)
            yield scrapy.Request(next_url, callback = self.parse)

        # 第二种写法：直接从response获取需要爬取的连接，并发送请求处理，直到链接全部提取完
        #if len(response.xpath("//a[@class='noactive' and @id='next']")) == 0:

            #url = response.xpath("//a[@id='next']/@href").extract()[0]
            #yield scrapy.Request("http://hr.tencent.com/" + url, callback = self.parse)