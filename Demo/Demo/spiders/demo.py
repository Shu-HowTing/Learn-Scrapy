# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from Demo.items import DemoItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    #allowed_domains = ['python123.io']
    start_urls = ["https://movie.douban.com/top250?start=0"]
    def parse(self, response):
        #fname = response.url.split('/')[-1]
        #with open (fname, 'wb') as f:
        #f.write(response.body)
        #self.log("Saved file %s. " % name)
        #item = DemoItem()
        self.soup = BeautifulSoup(response.body, 'html.parser')
        ol = self.soup.find('ol',class_ ="grid_view")
        li = ol.find_all('li')
        for l in li:
            try:
                item = DemoItem()
                span = l.find('span', class_="title")
                item['title'] = span.get_text()
                print(span.get_text())
                #title_list.append(title)
                p = l.find('p', class_="")
                item['director'] = p.get_text().split()[1]
                #director_list.append(director)
                spa = l.find('span', class_ = "inq")
                if spa is None:
                    item['quote'] = '########'
                else:
                    item['quote'] = spa.get_text()
                #introduce_list.append(quote)

                yield item



            except:
                continue

