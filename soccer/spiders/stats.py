# http://www.espnfc.com/english-premier-league/23/statistics/performance
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from soccer.items import SoccerItem

class general_info(scrapy.Spider):
	name = "genStats"

	start_urls = ["http://www.espnfc.com/english-premier-league/23/statistics/performance"]

	
	def parse(self, response):

		item = SoccerItem()

		item['mostWatchedLogo'] = response.xpath('//*[@id="stats-performance"]/div[1]/div[1]//img//@src').extract()
		mwt = response.xpath('(//*[@id="stats-performance"]/div[1]/div[1]/div/p[3]/text())').extract()
		for m in mwt:
			item['mostWatchedTeam'] = m.strip()

		item['mostHomeGoalsLogo'] = response.xpath('//*[@id="stats-performance"]/div[2]/div/div[1]/div/div[1]/div[1]/span/img//@src').extract()
		item['mostHomeGoalsTeam'] = response.xpath('//*[@id="stats-performance"]/div[2]/div/div[1]/div/div[1]/div[2]/span/img/@src').extract()



		return item



# 	# Largest Attendance
# 	response.xpath('//*[@id="stats-performance"]/div[1]/div[1]//img').extract();
#     response.xpath('//*[@id="stats-performance"]/div[1]/div[1]/div/p[3]/text()')


# Highest Home Scoring
#Teams 1 logo = response.xpath('//*[@id="stats-performance"]/div[2]/div/div[1]/div/div[1]/div[1]/span/img').extract()
#Teams 2 logo = response.xpath('//*[@id="stats-performance"]/div[2]/div/div[1]/div/div[1]/div[2]/span/img/@src').extract()

# Highes Away Scoring Game


