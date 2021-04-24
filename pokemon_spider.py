# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:58:46 2021

@author: clegg
"""


import scrapy

class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    
    start_urls = {
        'https://fevgames.net/pokedex/'
        }
    
    def parse(self, response):
        for entry in response.css('a.pokedex-item'):
            
            #this will extract the html containing the name and number,
            # split on the <br> elements
            data = entry.get().split('<br>')
            
            #extract the name from the html
            name = data[2][0:]
            
            #extract the number from the html
            number = data[1][1:]
         
            #get the link to the page for this pokemon
            page_link = entry.css('::attr(href)').get()
            
            #make a request for the pokemon description page
            request = response.follow(page_link, callback=self.parse_page)
            
            #add in the name and number
            request.cb_kwargs['name'] = name
            request.cb_kwargs['number'] = number
            
            yield request
            
            
    def parse_page(self, response, name, number):
        
        #extract the data holding the description text
        data = response.css("div.panel-body::text").getall()
        
        #get rid of all the superfluous stuff
        descr = ''.join(data).strip()
        
        yield {
            'name' : name,
            'number' : number,
            'description' : descr
            }