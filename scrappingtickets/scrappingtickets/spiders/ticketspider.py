import scrapy
import random

# "https://axs.com/artists/1108532/kiltro-tickets"

class TicketspiderSpider(scrapy.Spider):
    name = "ticketspider"
    allowed_domains = ["axs.com"]
    start_urls = "https://axs.com/artists/1108532/kiltro-tickets"

    async def start(self):
        yield scrapy.Request(
            self.start_urls,
            meta={
                "playwright": True,
                "playwright_include_page": True,
            },
            callback=self.parse, # what function is called after
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]

        while True:
            try:
                # wait for the button (short timeout so loop can break)
                await page.wait_for_selector('button[data-testid="SeeMoreButton"]', timeout=1000)

                await page.click('button[data-testid="SeeMoreButton"]')
                # wait for new items to load
                await page.wait_for_selector('[data-testid="MusicEventItemCard"]')
                self.logger.info("Clicked 'Load More'")
            except Exception:
                # if no button found break out of the loop
                self.logger.info("No more 'Load More' button found")
                break

        # get the final HTML
        html = await page.content()
        await page.close()

        # create a new Scrapy response from the final HTML
        response = response.replace(body=html)

        tickets = response.css('[data-testid="MusicEventItemCard"]')
        for ticket in tickets:
            yield {
                "date": ticket.css('[data-testid="ItemCardDate"] span::text').getall(),
                "loc": ticket.css('[data-testid="ItemCardLocation"] span::text').get(),
                "id": ticket.css('a::attr(href)').extract()
            }