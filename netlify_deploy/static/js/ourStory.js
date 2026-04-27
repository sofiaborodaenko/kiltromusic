import { loadNav } from "./nav.js";

loadNav();

const wrapper = document.querySelector(".wrapper");

console.log("WORKiNG");

console.log(document.body.scrollHeight, window.innerHeight);

wrapper.addEventListener("scroll", function () {
  const scrolled = wrapper.scrollTop;
  const video = document.querySelector(".parallax-video");

  console.log(scrolled);
});
