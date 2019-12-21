import scrapy
from stack_overflow.items import StackOverflowItem
# from scrapy import Spider
from scrapy.selector import Selector
from stack_overflow.items import StackOverflowItem


class StackSpider(scrapy.Spider):
    name = "stack"  # This defines the name of the spider we created
    allowed_domains = ['stackoverflow.com']  # We define the base_url for the allowed domains our spider is allowed to crawl
    # start_urls = ["https://stackoverflow.com/questions?pagesize=50&sort=newest",]

    def start_requests(self):
        yield scrapy.Request("https://stackoverflow.com/questions", self.parse)

    def parse(self,response):
        questions = response.xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = StackOverflowItem()
            item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract() # We assign the title to the summary text
            item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract() # We assign the hyperlink to the URL
            yield item

        # for h3 in response.xpath('//h3').getall():
        #     yield StackOverflowItem(title = h3)
        #
        # for href in response.xpath('//a/@href').getall():
        #     yield StackOverflowItem(url = response.urljoin(href))


