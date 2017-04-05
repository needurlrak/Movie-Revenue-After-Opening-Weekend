import scrapy


class ImdbSpider(scrapy.Spider):
    name = "movielist"
    start_urls = ['http://www.imdb.com/list/ls057823854/?start=1&view=detail&sort=listorian:asc']

    def parse(self, response):

        for i in response.xpath('//div[@class="list detail"]/div[contains(@class, "list_item")]'):
           # stars = []
            #for star in i.xpath('.//div[@class="secondary"][contains(text(),"Stars")]/a'):
             #   stars.append(star.xpath('./text()').extract_first)
            
            yield {
            'rank' : i.xpath('./div[@class="number"]/text()').extract_first(),
            'title' : i.xpath('./div[@class="info"]/b/a/text()').extract_first(),
            'year' : i.xpath('./div[@class="info"]/b/span/text()').extract_first().replace('(','').replace(')',''),
            'link' : i.xpath('./div[@class="info"]/b/a/@href').extract_first().replace('(','').replace(')',''),
            'rating' :i.xpath('.//span[@class="rating-rating"]/span[@class="value"]/text()').extract_first(),
            'director': i.xpath('.//div[@class="secondary"][contains(text(),"Director")]/a/text()').extract_first(),
            'stars': i.xpath('.//div[@class="secondary"][contains(text(),"Stars")]/a/text()').extract(),
            'description_runtime': i.xpath('.//div[@class="item_description"]').extract_first()
            }
    
        url = response.xpath('//div[@class="pagination"]/a[contains(text(),"Next")]/@href').extract_first()
        next_page = "http://www.imdb.com/list/ls057823854" + url

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
            
            
                
                