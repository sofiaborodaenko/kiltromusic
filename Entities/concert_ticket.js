export class ConcertTicket {
    #id;
    #featuredBand;
    #date;
    #timestamp;
    #location;

    constructor(id, featuredBand, date, timestamp, location) {
        this.#id = id;
        this.#featuredBand = featuredBand;
        this.#date = date;
        this.#timestamp = timestamp;
        this.#location = location;
    }

    setFeaturedBand(featuredBand) {
        this.#featuredBand = featuredBand;
    }

    getId() {
        return this.#id;
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