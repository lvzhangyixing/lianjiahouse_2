import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy
from ..items import Lianjiahouse2Item



class HouseSpider(CrawlSpider):
    name = 'house'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/']

    rules = (
        Rule(LinkExtractor(allow='/ershoufang/\d{12}.html'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = Lianjiahouse2Item()
        # 二手房名称
        i['house_name'] = response.css('title::text').extract_first().replace(' ','')
        # 所在小区
        i['community_name'] = response.css('.communityName a::text').extract_first()
        # 链家编号
        i['house_record'] = response.css('houseRecord .info::text').extract_first()
        # 总价
        i['total_amount'] = response.css('.overview .total::text').extract_first()
        # 单价
        i['unit_price'] = response.css('.unitPriceValue::text').extract_first()

        # 挂牌时间
        i['release_date'] = response.xpath('//div[@class="transaction"]//ul/li[1]'
                                           '/span[2]/text()').extract_first()

        # 图片url
        i['images_urls'] = response.css('.smallpic > li::attr(data-pic)').extract()
        yield i
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
