#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 17:40:32 2017

@author: karlrudeen
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 18:51:24 2017

@author: karlrudeen
"""

import scrapy
import time


class ImdbSpider(scrapy.Spider):
    name = "the_numbers_spider"
    start_urls = [
    'http://www.the-numbers.com/movie/budgets/all'
    ]

    def parse(self, response):

        for obj in response.xpath('//table/tr'):
            #time.sleep(.01)
            if obj.xpath('./td/b/a/text()').extract_first() is not None:
                yield{
                    'title' : obj.xpath('./td/b/a/text()').extract_first(),
                    'release_date' : obj.xpath('./td/a/text()').extract_first(),
                    'production_budget' : obj.xpath('./td[4]/text()').extract_first(),
                    'domestic_gross(numbers)' : obj.xpath('./td[5]/text()').extract_first(),
                    'worldwide_gross(numbers)' : obj.xpath('./td[6]/text()').extract_first(),
                    'rank' : obj.xpath('./td[1]/text()').extract_first()
                      }
                
                
                