import scrapy

from scrapy.http import Request
from scrapy.selector import Selector
from meirenyu.items import meirenyuItem
from scrapy.selector import Selector


class meirenyuSpider(scrapy.Spider):
    name = 'meirenyu'
    allowed_domains = ['douban.com']

    start_urls = ['http://movie.douban.com/subject/19944106/comments']

    def parse(self, response):
        sel = Selector(response)
        self.log('Hi,this is an item page! %s' % response.url)
        item = meirenyuItem()

        item['comment'] = sel.xpath(
            '//div[@class = "comment"]/p[@class = ""]/text()[1]').extract()

    item['grade'] = sel.xpath(
        '//div[@class = "comment"]/h3/span[@class = "comment-info"]/span[contains(@class, "allstar")]/@title').extract()
    yield item

    next_page = '//div[@id = "paginator"]/a[@class="next"]/@href'
    if response.xpath(next_page):
        url_nextpage = 'http://movie.douban.com/subject/19944106/comments' + \
            response.xpath(next_page).extract()[0]
        request = scrapy.Request(url_nextpage, callback=self.parse)
        yield request
