import { loadNav } from "./nav.js";

loadNav();

const srcollers = document.querySelectorAll(".scroller");
const allRevealSections = document.querySelectorAll(".reveal_section");

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
  threshold: 0.15,
});

allRevealSections.forEach(function (section) {
  sectionObserver.observe(section);
  section.classList.add("section--hidden");
});
