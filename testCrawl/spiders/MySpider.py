import scrapy

from testCrawl.items import TestcrawlItem
import sys

class MyspiderSpider(scrapy.Spider):
    name = "spiderCar"
    allowed_domains = ["cartalk.com"]
    # 填写爬取地址
    start_urls = [
        "https://community.cartalk.com/",
    ]

    # 编写爬取方法
    def parse(self, response):
        for line in response.xpath('//tr[@class="topic-list-item"]'):
            # 初始化item对象保存爬取的信息
            item = TestcrawlItem()
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['title'] = line.xpath(
                './/td[contains(@class,"main-link")]//span[contains(@class,"link-top-line")]/a/text()').extract()
            item['car'] = line.xpath(
                './/td[contains(@class,"main-link")]//div[contains(@class,"link-bottom-line")]'
                '//div[contains(@class,"discourse-tags")]/a/text()').extract()
            item['reply'] = line.xpath(
                './/td[contains(@class,"replies")]/span/text()').extract()
            yield item