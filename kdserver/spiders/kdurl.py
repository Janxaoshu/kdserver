import scrapy

from kdserver import items


class KdUrl(scrapy.Spider):
    name = "app"
    allowed_domains = ["acg.gamersky.com"]
    start_urls = ["http://acg.gamersky.com/hot/"]


    def parse(self, response):

        url = response.xpath('//ul[@class=\'pictxt block contentpaging\']/li[@class=\'ptxt\']')
        for sel in url:
            item = items.KdserverItem()
            item['title'] = sel.xpath('div[@class=\'tit\']/a/text()').extract()
            item['subject'] = sel.xpath('div[@class=\'con\']/div[@class=\'txt\']').extract()
            yield item
