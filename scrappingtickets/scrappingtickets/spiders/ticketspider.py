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
            date_parts = ticket.css('[data-testid="ItemCardDate"] span::text').getall()[1:4]
            date = ' '.join(date_parts)
            yield {
                "date": date,
                "band": ticket.css('div[class*=styles__ItemCardTitle] span::text').get(),
                "featured band": ticket.css('div[class*=styles__FeaturedArtists] span::text').get(),
                "loc": ticket.css('[data-testid="ItemCardLocation"] span::text').get(),
                "id": ticket.css('a::attr(href)').extract()
            }


            # sc-dOfePm ckrUXz c-axs-block Div-sc-6uq8dp hcZwzU c-axs-flex-item styles__ItemCardTitle-sc-e04a8803-11 kIAxPi

            # sc-gnOvAp fmkLZT c-axs-block Div-sc-6uq8dp hcZwzU c-axs-flex-item styles__ItemCardTitle-sc-7d42833d-11 kSEuOg



            # styles__FeaturedArtists-sc-7d42833d-6 gIxoFL

            # styles__FeaturedArtists-sc-e04a8803-6 bdjAUd