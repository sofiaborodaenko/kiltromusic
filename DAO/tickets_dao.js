import { AllTickets } from "../Entities/all_tickets.js";
import { ConcertTicket } from "../Entities/concert_ticket.js";

export class TicketsDAO {

  constructor(allTickets) {
    this.allTickets = allTickets;
    this.concertTicket = new ConcertTicket();
  }

    async populateTickets() {

        try {
            const response = await fetch("../scrappingtickets/ticketdata.json");
            const data = await response.json();

            data.forEach(ticket => {
                this.concertTicket = new ConcertTicket(ticket["id"][0], ticket["band"], ticket["featuredBand"], ticket["date"], ticket["timestamp"], ticket["loc"]);
                this.allTickets.addTicket(this.concertTicket);
            });

        } catch (error) {
            console.error("Error fetching ticket data:", error);
        }

    }

}
