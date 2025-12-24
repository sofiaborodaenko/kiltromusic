export class ConcertTicket {
    #id;
    #band;
    #featuredBand;
    #date;
    #timestamp;
    #location;
    #linkId;

    constructor(id, band, featuredBand, date, timestamp, location, linkId) {
        this.#id = id;
        this.#band = band;
        this.#featuredBand = featuredBand;
        this.#date = date;
        this.#timestamp = timestamp;
        this.#location = location;
        this.#linkId = linkId;
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

    getLinkId() {
        return this.#linkId;
    }
}