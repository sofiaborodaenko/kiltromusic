import { loadNav } from "./nav.js";
import { TicketsDAO } from "../../DAO/tickets_dao.js";
import { AllTickets } from "../../Entities/all_tickets.js";

loadNav();

class LiveEvents {
    #tickets = [];

    constructor() {
        this.AllTickets = new AllTickets();
    }

    getEvents() {

        if (this.#tickets.length === 0) {
            this.#tickets = this.AllTickets.getTickets();
            return this.#tickets;
        } else if (this.#tickets === this.AllTickets.getTickets()) {
          return this.#tickets;
        } else {
          return this.AllTickets.getTickets();
        }

    }

}

document.addEventListener("DOMContentLoaded", () => {
    const liveEvents = new LiveEvents();
    const ticketsDAO = new TicketsDAO(); 
    console.log(liveEvents.getEvents());
    ticketsDAO.populateTickets();
});



