import scrapy

class NewsSpider(scrapy.Spider):
    name='newsspider'
    allowed_domain=['thehimalayantimes.com']
    start_urls=['https://thehimalayantimes.com/']

    def parse(self, response):
        list_news_types=['Economics','Politics','Crime','Sports','International','National']
        title=response.css('title::text').extract()
        yield {'titletext':title}
        

