# -*- coding: utf-8 -*-
import json
import os

import scrapy
from ..items import DouyuItem

class DySpider(scrapy.Spider):
    name = 'dy'
    allowed_domains = ['www.douyu.com','rpic.douyucdn.cn']
    start_urls = ['https://www.douyu.com/gapi/rknc/directory/yzRec/1']

    def parse(self, response):
        json_ = json.loads(response.text)
        all = json_.get('data').get('rl')

        for info in all:
            item = DouyuItem()
            # 封面小图url
            item['title'] = info.get('rn').replace('\n','')
            item['img_url'] = info.get('rs16')
            yield item
    #         yield scrapy.Request(url=item['img_url'],callback=self.save_img,meta={'item':item})
    #
    # def save_img(self,response):
    #     if not os.path.exists('images'):
    #         os.makedirs('images')
    #     with open('images/'+response.meta['item']['title']+'.jpg','wb') as f:
    #         f.write(response.body)





