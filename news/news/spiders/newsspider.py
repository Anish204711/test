import scrapy

class NewsSpider(scrapy.Spider):
    name='newsspider'
    allowed_domain=['thehimalayantimes.com']
    start_urls=['https://thehimalayantimes.com/']

    def parse(self, response):
        response.css('h3.alith_post_title a::text').extract()
        response.css('li.pager-nav  a::attr("href")').extract()
        list_news_types=['Economics','Politics','Crime','Sports','International','National']
        title=response.css('title::text').extract()
        yield {'titletext':title}
        

