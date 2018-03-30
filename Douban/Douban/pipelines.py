# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#保存为JSON
import json

class DoubanPipeline(object):
    def __init__(self):
        self.f = open("top250.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(item, ensure_ascii = False) + ",\n"
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()




# #保存为CSV
# from scrapy.exporters import CsvItemExporter
# class DoubanPipeline(object):
#     def open_spider(self, spider):
#         self.file = open('top250.csv', 'wb')
#         self.exporter = CsvItemExporter(self.file)
#         self.exporter.start_exporting()

#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item

#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.file.close()

