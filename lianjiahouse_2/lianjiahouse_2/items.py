# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lianjiahouse2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 发布信息名称
    house_name = scrapy.Field()
    # 小区名称
    community_name = scrapy.Field()
    # 所在区域
    # location = scrapy.Field()
    # 链家编号
    house_record = scrapy.Field()
    # 总售价
    total_amount = scrapy.Field()
    # 单价
    unit_price = scrapy.Field()

    # 房屋基本信息
    # 建筑面积
    # area_total = scrapy.Field()

    # 房屋交易信息
    release_date = scrapy.Field()
    # 图片地址
    images_urls = scrapy.Field()
    # 保存图片
    images = scrapy.Field()