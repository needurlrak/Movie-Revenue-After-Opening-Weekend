#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 18:51:24 2017

@author: karlrudeen
"""

import scrapy


class ImdbSpider(scrapy.Spider):
    name = "openingWeekend"
    start_urls = [
    'http://www.boxofficemojo.com/alltime/weekends/?adjust_yr=2016&p=.htm'
    ]

    def parse(self, response):

        for obj in response.xpath('//table[@width = "98%"]/tr'):
            yield{
                'title' : obj.xpath('./td/font/a/b/text()').extract_first(),
                'adjusted_opening' : obj.xpath('./td/font/b/text()').extract_first(),
                'percent_of_total' : obj.xpath('./td[5]/font/text()').extract_first(),
                'theaters' : obj.xpath('./td[6]/font/text()').extract_first(),
                'average_per_theater' : obj.xpath('./td[7]/font/text()').extract_first(),
                'adjusted_gross' : obj.xpath('./td[8]/font/text()').extract_first(),
                'date' : obj.xpath('./td[9]/font/a/text()').extract_first()
                  }
                  
        url = response.xpath('//a[contains(text(),"Next")]/@href').extract_first()
        
        if url is not None:
            next_page = 'http://www.boxofficemojo.com/' + url
    
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
                
                