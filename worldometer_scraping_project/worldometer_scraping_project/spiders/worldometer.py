import scrapy


class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        page_title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath('.//text()').get()
            country_link = country.xpath('.//@href').get()

            # Create absolute link using concatenation as relative will not work with Request method
            # absolute_url = f'https://www.worldometers.info/{country_link}'

            # Create absolute link using urljoin method
            absolute_url = response.urljoin(country_link)
            # yield scrapy.Request(url=absolute_url)

            # Use relative url with follow method
            # yield response.follow(url=country_link)

            # Scrape data from multiple links, pass country name to parse each country function
            yield response.follow(url=country_link, callback=self.parse_each_country, meta={'Country': country_name})

    def parse_each_country(self, response):
        """Parses each individual country page to retrieve country year and population"""
        # response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        # Retrieve country name value from meta argument
        country = response.request.meta['Country']
        rows = response.xpath("(//table[contains(@class, 'table')])[1]/tbody/tr")
        for row in rows:
            # Retrieve the year text from row of data
            year = row.xpath('.//td[1]/text()').get()
            # Retrieve the population text from row of data
            population = row.xpath('.//td[2]/strong/text()').get()

            yield {
                'Country': country,
                'Year': year,
                'Population': population
            }