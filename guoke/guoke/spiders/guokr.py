# -*- coding: utf-8 -*-
import scrapy
from ..items import GuokeItem

class GuokrSpider(scrapy.Spider):
    name = 'guokr'
    allowed_domains = ['www.guokr.com']
    start_urls = ['http://www.guokr.com/']

    def parse(self, response):
        node_list = response.xpath('//div[@class="FeedFloat__FeedFloatWrap-zt5yna-0 cHPaIe"]//a/div')
        item = GuokeItem()
        # print(response.text)
        for node in node_list:
            item['title'] = node.xpath('./div[2]/div[2]/text()').extract()[0]
            item['content'] = node.xpath('./div[2]/div[3]/span/text()').extract()[0]
            # img = node.xpath('./div[1]/div/img/@src').extract()
            item['type_'] = ' '.join(node.xpath('div[2]/div[1]/span/text()').extract())


            yield item



