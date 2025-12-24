import { AllTickets } from "../Entities/all_tickets.js";
import { ConcertTicket } from "../Entities/concert_ticket.js";

export class TicketsDAO {

  constructor() {
    this.AllTickets = new AllTickets();
    this.ConcertTicket = new ConcertTicket();
  }

  populateTickets() {
    fetch("../scrappingtickets/ticketdata.json")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => console.error("Error fetching ticket data:", error));
  }
}
