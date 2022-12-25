import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/scrapy/']
    start_urls = ['https://www.reddit.com/r/scrapy/']

    def parse(self, response):
        print("getting titles")
        titles = response.css("._eYtD2XCVieq6emjKBH3m::text").extract()
        votes = response.css("._1rZYMD_4xY3gRcSS3p8ODO._3a2ZHWaih05DgAOtvu6cIo::text").extract()
        comments = response.css(".FHCV02u6Cp2zYL0fhQPsO::text").extract()

        for item in zip(titles, votes, comments):
            scraped_info = {
                'title': item[0],
                'vote': item[1],
                'comments': item[2],
            }
            yield scraped_info
