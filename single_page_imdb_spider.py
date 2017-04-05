#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 20:21:23 2017

@author: karlrudeen
"""

import scrapy
import re
import pandas as pd

class ImdbSinglePageSpider(scrapy.Spider):
    name = "specificPageScrape"
   
    #start_urls = ['http://www.imdb.com/list/ls057823854/?start=1&view=detail&sort=listorian:asc']

    def start_requests(self):
        df = pd.read_csv('imdb_info_6.csv')
        urls = list(df['link'])
        
        for url in urls:
            yield scrapy.Request(url='http://www.imdb.com' + url, callback = self.parse)

    def parse(self, response):
        page = response.text
      #  gross = ""
        budget = ""
        release_date = ""
       # opening_weekend = ""
#        if page is not None:
#            a = re.search(r'Gross:</h4>[ ]+[$][0-9,]+', page)
#            if a is not None:
#                b = re.search(r'[$][0-9,]+', a.group(0))
#                if b is not None:
#                    gross = b.group(0)[1:]

        a1 = re.search(r'Budget:</h4>[ ]+[$][0-9,]+', page)
        if a1 is not None:
            b1 = re.search(r'[$][0-9,]+', a1.group(0))
            if b1 is not None: 
                budget = b1.group(0)[1:]
        a2 = re.search(r'Release Date:</h4>[ ]+[0-9,a-z A-Z]+', page)
        if a2 is not None :
            b2 = re.search(r'>[ ][0-9,a-z A-Z]+', a2.group(0))
            if b2 is not None:
                release_date = b2.group(0)[1:]
#        a3 = re.search(r'Opening Weekend:</h4>[ ]+[$][0-9,]+', page)
#        if a3 is not None :
#            b3 = re.search(r'[$][0-9,]+', a3.group(0))
#            if b3 is not None:
#                opening_weekend = b3.group(0)[1:]
        yield {
           # 'gross' : gross,
            'title' : response.xpath('.//div[@class="title_wrapper"]/h1/text()').extract_first().strip(' '),
            'budget' : budget,
            'release_date' : release_date,
            #'opening_weekend' : opening_weekend,
            'metascore' : response.xpath('.//div[contains(@class, "metacriticScore")]/span/text()').extract_first()
            }