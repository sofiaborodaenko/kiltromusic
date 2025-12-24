import { loadNav } from "./nav.js";
import { TicketsDAO } from "../../DAO/tickets_dao.js";
import { AllTickets } from "../../Entities/all_tickets.js";

loadNav();

class LiveEvents {

    constructor(allTickets) {
        this.allTickets = allTickets;
    }

    getEvents() {
        return this.allTickets.getTickets();

    }

}

document.addEventListener("DOMContentLoaded", async () => {
    const allTickets = new AllTickets();
    const ticketsDAO = new TicketsDAO(allTickets); 
    const liveEvents = new LiveEvents(allTickets);
    
    await ticketsDAO.populateTickets();
    console.log(liveEvents.getEvents());
    
});



