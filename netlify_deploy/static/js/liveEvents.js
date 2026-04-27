import { loadNav } from "./nav.js";
import { TicketsDAO } from "../../DAO/tickets_dao.js";
import { AllTickets } from "../../Entities/all_tickets.js";

loadNav();

export class LiveEvents {

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
    renderTickets(allTickets.getTickets());
    
});

export function renderTickets(tickets, max = tickets.length) {
    const container = document.getElementById("live_events_container");
    container.innerHTML = "";

    if (tickets.length === 0) {
        container.innerHTML = `
            <div class="no__events">
            <p>No upcoming events at the moment. Please check back later.</p>
            </div>
        
        `;
        return;
    }

    tickets.splice(0, max).forEach(ticket => {
        const ticketElement = document.createElement("div");
        ticketElement.classList.add("event__dates");
        ticketElement.innerHTML = `
            <div class="date">
            <p class="emphasize bold"> ${ticket.getDate()}</p>
            <p>w/ ${ticket.getFeaturedBand()}</p>
            </div>
            <p>${ticket.getLocation()}</p>
            <button class="main__button" onclick="window.open('https://www.axs.com${ticket.getId()}', '_blank')">Buy Tickets</button>
        `;
        container.appendChild(ticketElement);
    });
    
}



