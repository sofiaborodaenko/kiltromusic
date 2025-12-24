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
    renderTickets(allTickets.getTickets());
    
});

function renderTickets(tickets) {
    const container = document.getElementById("live_events_container");
    container.innerHTML = "";

    tickets.forEach(ticket => {
        const ticketElement = document.createElement("div");
        ticketElement.classList.add("event__dates");
        ticketElement.innerHTML = `
            <div class="date">
            <p class="emphasize bold"> ${ticket.getDate()}</p>
            <p>w/ ${ticket.getFeaturedBand()}</p>
            </div>
            <p>${ticket.getLocation()}</p>
            <button class="main__button" onclick="window.location.href='https://www.axs.com${ticket.getId()}'">Buy Tickets</button>
        `;
        container.appendChild(ticketElement);
    });

    
}



