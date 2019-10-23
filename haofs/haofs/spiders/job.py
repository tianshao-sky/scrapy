# -*- coding: utf-8 -*-
import scrapy
from ..items import HaofsItem


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['job.haofs.com']
    start_urls = ['http://job.haofs.com/list.asp?p=1']

    def parse(self, response):
        node_list = response.xpath('//div[@class="job_listpage"][2]/ul')
        # item = HaofsItem()

        for node in node_list:
            item = HaofsItem()
            item['name'] = node.xpath('./li[1]/a/text()').extract_first()
            item['company'] = node.xpath('./li[2]/a/text()').extract()[0]
            item['location'] = node.xpath('./li[3]/font/text()').extract()[0]
            item['num'] = node.xpath('./li[3]/font/text()').extract()[1]
            item['salary'] = node.xpath('./li[4]/text()').extract()[0]
            item['nature'] = node.xpath('./li[5]/text()|./li[5]/font/text()').extract()[0]
            item['update_time'] = node.xpath('./li[6]/font/text()|./li[6]/text()').extract()[0]
            next_url = 'http://job.haofs.com/'+node.xpath('./li[1]/a/@href').extract_first()
            # yield item
            yield scrapy.Request(url=next_url,callback=self.detail_parse,meta={"sss":item})

        if int(response.request.url[-1]) < 1:
            yield scrapy.Request(url=response.request.url[:-1]+str(int(response.request.url[-1])+1))
        # flag = response.xpath('//div[@class="showpage f12"]/ul/li[last()]/a/@href').extract_first()
        # if flag:
        #     next_url = "http://job.haofs.com/"+flag
        #     yield scrapy.Request(url=next_url)

    def detail_parse(self,response):
        item = response.meta['sss']
        item['info'] = response.xpath('//ul[@id="zptext"]/text()').extract()[0]

        yield item


