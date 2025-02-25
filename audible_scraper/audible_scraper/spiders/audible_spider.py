import scrapy


class AudibleSpiderSpider(scrapy.Spider):
    name = "audible_spider"
    allowed_domains = ["www.audible.co.uk"]
    # start_urls = ["https://www.audible.co.uk/search"]

    def start_requests(self):
        """Change user-agent for requests"""
        yield scrapy.Request(url="https://www.audible.co.uk/search", callback=self.parse,
                             headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                                    '(KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'})

    def parse(self, response):
        product_container = response.xpath("(//div[@class='adbl-impression-container '])"
                                           "//li[contains(@class, 'productListItem')]")

        for product in product_container:
            title = product.xpath(".//h3[contains(@class, 'bc-heading')]/a/text()").get()
            author = product.xpath(".//li[contains(@class, 'authorLabel')]/span/a/text()").getall()
            length = product.xpath(".//li[contains(@class, 'runtimeLabel')]/span/text()").get()

            yield {
                'Title': title,
                'Author': author,
                'Length': length,
                'User-Agent': response.request.headers['User-Agent']
            }

            pagination_bar = response.xpath(".//ul[contains(@class, 'pagingElements')]/li")
            next_page_url = pagination_bar.xpath(".//span[contains(@class, 'nextButton')]/a/@href").get()
            button_disabled = pagination_bar.xpath(".//span[contains(@class, 'nextButton')]/a/@aria-disabled").get()

        # Go to next page if exists and scrape data
        if next_page_url and button_disabled==None:
            yield response.follow(url=next_page_url, callback=self.parse, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                                    '(KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'})
