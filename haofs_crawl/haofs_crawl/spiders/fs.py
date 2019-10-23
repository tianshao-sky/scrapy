# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FsSpider(CrawlSpider):
    name = 'fs'
    allowed_domains = ['job.haofs.com']
    start_urls = ['http://job.haofs.com/list.asp?p=1']

    rules = (
        Rule(LinkExtractor(allow=r'company\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        print(response.xpath('//ul[@class="green f24 fb fyhei"]/text()').extract()[1].strip('\\xa0').strip())
        # return item
