import scrapy
from ..items import NewsItem
class NewsSpider(scrapy.Spider):
    name='newsspider'
    allowed_domain=['thehimalayantimes.com']
    start_urls=['https://thehimalayantimes.com/search?query=politics',
                'https://thehimalayantimes.com/search?query=economics',
                'https://thehimalayantimes.com/search?query=internationals',
                'https://thehimalayantimes.com/search?query=sports',
                ]
    

    def parse(self, response):
        
        # list of all available news links in a page.
        news_detail_links=response.css(".animated-fast a::attr('href')").extract()
        for link in news_detail_links:
            yield response.follow(link, callback=self.parse_link)
        # i=0
    
        #next_page=new_link+'&pgno='+str(i+1)
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

    def parse_link(self, response):
        items=NewsItem()
        news_title=response.css('h1.alith_post_title::text').extract()
        news_author=response.css('div.article_author_name::text').extract()
        news_date=response.css('div.article_date::text').extract() 
        news_content=response.css('article div.post-content div.single-content div.animate-box').extract()
       
        # Adding data to items
        items['title']=news_title
        items['author']=news_author
        items['date']=news_date
        items['content']=news_content
        return items
        
        
                
        

