import scrapy


class DebtsSpider(scrapy.Spider):
    name = "debts"
    allowed_domains = ["worldpopulationreview.com"]
    start_urls = ["https://worldpopulationreview.com/country-rankings/countries-by-national-debt"]

    def parse(self, response):
        countries = response.xpath('(//table[@class="tp-table-body is-narrow w-full min-w-full table-auto border-separate border-spacing-0 border bg-white"])[3]/tbody/tr[position() != 0 ]')
        
        for country in countries:
            name = country.xpath(".//th/a/text()").get()
            debt = country.xpath(".//td[1]/text()").get()
            yield {
                'country' : name,
                'debt': debt
            } 

