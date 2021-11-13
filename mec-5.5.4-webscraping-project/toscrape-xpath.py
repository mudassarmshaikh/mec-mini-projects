import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"
    #start_urls = [
    #    'http://quotes.toscrape.com/page/1/',
    #    'http://quotes.toscrape.com/page/2/',
    #    ]

    #def start_requests(self):
    #    urls = [
    #    'http://quotes.toscrape.com/page/1/',
    #    'http://quotes.toscrape.com/page/2/',
    #    ]
    #   for url in urls:
    #       yield scrapy.Request(url=url, callback=self.parse)

    def start_requests(self):
        url = 'https://quotes.toscrape.com/'

        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.xpath("//div[@class='container']"):
            print(quote)
            yield {
                'text': quote.xpath('//div/span/text()').get(),
                'author': quote.xpath('//div/span/small/text()').get(),
                'tags': quote.xpath('//div/tags //a/tag/text()').getall(),
                }
    
        #next_page = response.xpath('//li/next //a/attr(href)').get()
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse)
        #    yield response.follow(next_page, callback=self.parse)
