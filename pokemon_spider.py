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
            yield {
                'name' : entry.re('<br>(\w+)<br>'),
                'number' : entry.re('<br>#(\d+)<br>')
                }