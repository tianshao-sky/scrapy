# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem
from scrapy.utils.misc import md5sum

from .settings import IMAGES_STORE


class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return scrapy.Request(url=item['img_url'])

    def item_completed(self, results, item, info):
        img_name = IMAGES_STORE +'/'+ [x['path'] for ok,x in results if ok][0]
        new_name = IMAGES_STORE +'/full/'+ item['title']+'.jpg'

        os.rename(img_name,new_name)
        return item




