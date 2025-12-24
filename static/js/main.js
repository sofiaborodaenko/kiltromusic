import { loadNav } from "./nav.js";
import { AllTickets } from "../../Entities/all_tickets.js";
import { TicketsDAO } from "../../DAO/tickets_dao.js";
import { LiveEvents } from "../js/liveEvents.js";
import { renderTickets } from "../js/liveEvents.js";

loadNav();

const srcollers = document.querySelectorAll(".scroller");
const allRevealSections = document.querySelectorAll(".reveal_section");
const allMobileHoverSections = document.querySelectorAll(".mobile_hover");
// console.log(allMobileHoverSections);

// Infinite scroller

// Check if the user prefers reduced motion
if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  addAnimation();
}

// Add event listener to each scroller
function addAnimation() {
  srcollers.forEach((scroller) => {
    scroller.setAttribute("data-animated", true);

    const scrollerInner = scroller.querySelector(".scroller__inner");
    const scrollerContent = Array.from(scrollerInner.children);

    scrollerContent.forEach((item) => {
      const duplicatedItem = item.cloneNode(true);
      // makes sure screen reader doesnt read all of them
      duplicatedItem.setAttribute("aria-hidden", true);
      scrollerInner.appendChild(duplicatedItem);
    });
  });
}

// Reveal sections on scroll
const revealSection = function (entries, observer) {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;

    entry.target.classList.remove("section--hidden");
    observer.unobserve(entry.target);
  });
};

const sectionObserver = new IntersectionObserver(revealSection, {
  root: null,
  threshold: 0.25,
});

allRevealSections.forEach(function (section) {
  sectionObserver.observe(section);
  section.classList.add("section--hidden");
});

// Checks if user is on mobile or similar
const revealHiddenText = function (entries, observer) {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) {
      entry.target.lastElementChild.style.opacity = "0";
      return;
    }
    // console.log(entry);
    // console.log(entry.target.lastElementChild.classList);
    entry.target.lastElementChild.style.opacity = "1";
  });
};

const mobileObserver = new IntersectionObserver(revealHiddenText, {
  root: null,
  threshold: 0.7,
});

if (window.matchMedia("(hover: none)").matches) {
  allMobileHoverSections.forEach(function (section) {
    const parentDiv = section.parentNode;
    mobileObserver.observe(parentDiv);
  });
}

// Checks if user is on Safari to remove the fixed image scrolling problem
document.addEventListener("DOMContentLoaded", async function () {
  const ua = navigator.userAgent;
  const isSafari = /^((?!chrome|android).)*safari/i.test(ua); // true for Safari only

  if (isSafari) {
    document.body.classList.add("safari");
  }

  const allTickets = new AllTickets();
  const ticketsDAO = new TicketsDAO(allTickets);
  const liveEvents = new LiveEvents(allTickets);

  await ticketsDAO.populateTickets();

  renderTickets(allTickets.getTickets(), 2);
});
