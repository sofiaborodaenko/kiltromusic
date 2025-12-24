export class ConcertTicket {
    #id;
    #band;
    #featuredBand;
    #date;
    #timestamp;
    #location;

    constructor(id, band, featuredBand, date, timestamp, location) {
        this.#id = id;
        this.#band = band;
        this.#featuredBand = featuredBand;
        this.#date = date;
        this.#timestamp = timestamp;
        this.#location = location;
    }

    getId() {
        return this.#id;
    }

    getBand() {
        return this.#band;
    }

    getFeaturedBand() {
        return this.#featuredBand;
    }

    getDate() {
        return this.#date;
    }

    getTimestamp() {
        return this.#timestamp;
    }

    getLocation() {
        return this.#location;
    }
}