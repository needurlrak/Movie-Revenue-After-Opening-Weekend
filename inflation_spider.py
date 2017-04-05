#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 18:51:24 2017

@author: karlrudeen
"""

import scrapy


class ImdbSpider(scrapy.Spider):
    name = "inflation_spider"
    start_urls = [
    'http://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/'
    ]

    def parse(self, response):

        for obj in response.xpath('//table/tbody/tr'):
            yield{
                'year' : obj.xpath('./td/strong/text()').extract_first(),
                'CPI_index' : obj.xpath('./td[2]/text()').extract_first()
                  }
            
                
                