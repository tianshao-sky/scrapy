# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient


class HaofsPipeline(object):
    def open_spider(self,spider):
        self.f = open('job.json','w')
        # self.db = MongoClient().tests

    def process_item(self, item, spider):
        dict_data = dict(item)
        json_str = json.dumps(dict_data, ensure_ascii=False)
        self.f.write(json_str + '\n')

        # self.db.stu.insert(dict(item))
        return item

    def close_spider(self,spider):
        self.f.close()
