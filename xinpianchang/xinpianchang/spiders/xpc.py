# -*- coding: utf-8 -*-
import scrapy
from ..items import XinpianchangItem


class XpcSpider(scrapy.Spider):
    name = 'xpc'
    allowed_domains = ['www.xinpianchang.com']
    start_urls = ['http://www.xinpianchang.com/channel/index/sort-like']

    def parse(self, response):

        node_list = response.xpath('//div[@class="channel-con"]/ul/li')
        items = XinpianchangItem()
        for node in node_list:

            items["titles"] = node.xpath('./div/div/a/p/text()').extract()[0]
            items["watch_num"] = node.xpath('.//span[@class="fw_300 icon-play-volume"]/text()').extract()[0]

            yield items

