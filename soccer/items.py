# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SoccerItem(scrapy.Item):
    # define the fields for your item here like:
    mostWatchedLogo= scrapy.Field()
    mostWatchedTeam = scrapy.Field()
    mostHomeGoalsLogo = scrapy.Field()
    mostHomeGoalsTeam = scrapy.Field()
    pass




# 	# Largest Attendance
# 	response.xpath('//*[@id="stats-performance"]/div[1]/div[1]//img').extract();
#     response.xpath('//*[@id="stats-performance"]/div[1]/div[1]/div/p[3]/text()')


# Highest Home Scoring
#Teams 1 logo = response.xpath('//*[@id="stats-performance"]/div[2]/div/div[1]/div/div[1]/div[1]/span/img').extract()
#Teams 2 logo = response.xpath('//*[@id="stats-performance"]/div[2]/div/div[1]/div/div[1]/div[2]/span/img/@src').extract()
