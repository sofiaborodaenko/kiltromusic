export class AllTickets {
    #allTickets = [];

    addTicket(ticket) {
        this.#allTickets.push(ticket);
    }

    removeTicket(ticket) {
        this.#allTickets = this.#allTickets.filter(t => t !== ticket);
    }

    getTickets() {
        return this.#allTickets;
    }
}