import scrapy
import random


class TicketspiderSpider(scrapy.Spider):
    name = "ticketspider"
    allowed_domains = ["axs.com"]
    start_urls = ["https://axs.com/artists/1108532/kiltro-tickets"]

    def start(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={
                    "playwright": True,                     # render JS
                    "playwright_include_page": True,       # optional if you need the page object
                    "playwright_page_coroutines": [
                        {"name": "wait_for_selector", "args": ['[data-testid="MusicCard"]']}
                    ]
                }
            )

    async def parse(self, response):
        # what i want to extract
        tickets = response.css('[data-testid="MusicEventItemCard"]')
        
        for ticket in tickets:
            # yield response.follow(self.start_urls, callback=self.parse)

            yield {
                "ticket": ticket.get()
            }
