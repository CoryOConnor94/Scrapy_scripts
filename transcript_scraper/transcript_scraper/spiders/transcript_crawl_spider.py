import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptCrawlSpiderSpider(CrawlSpider):
    name = "transcript_crawl_spider"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com"]
    # Set download delay
    custom_settings = {
        'DOWNLOAD_DELAY': 0.8,
    }

    rules = (
        # Rule to scrap first page
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']//a")), callback="parse_item", follow=True),
        # Rule to go to next page after scraping current page
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]")))
    )

    def parse_item(self, response):
        article = response.xpath("//article[@class='main-article']")
        yield {
            'Title': article.xpath('./h1/text()').get(),
            'Plot': article.xpath('./p/text()').get(),
            # 'Transcript': article.xpath("./div[@class='full-script']/text()").getall(),
            'Url': response.url,
        }

