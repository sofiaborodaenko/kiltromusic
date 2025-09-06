import scrapy


class TicketspiderSpider(scrapy.Spider):
    name = "ticketspider"
    allowed_domains = ["axs.com"]
    start_urls = ["https://axs.com/artists/1108532/kiltro-tickets"]

    def parse(self, response):
        # what i want to extract
        pass
