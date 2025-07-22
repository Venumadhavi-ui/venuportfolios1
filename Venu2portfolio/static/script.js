

document.addEventListener("DOMContentLoaded", () => {
  const sections = document.querySelectorAll(".section");

  function revealSections() {
    const triggerBottom = window.innerHeight * 0.85;
    sections.forEach(section => {
      const sectionTop = section.getBoundingClientRect().top;
      if (sectionTop < triggerBottom) {
        section.classList.add("visible");
      }
    });
  }

  
  window.addEventListener("scroll", revealSections);
  window.addEventListener("load", revealSections);

  
  revealSections();
});
document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", function (e) {
      const gender = form.querySelector('input[name="gender"]:checked');
      const interests = form.querySelectorAll('input[name="interests"]:checked');
      const bio = form.querySelector('input[name="bio"]');

      if (!gender || interests.length === 0 || !bio.value.trim()) {
        e.preventDefault();
        alert("Please complete all fields before submitting the form.");
      }
    });
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({
        behavior: "smooth"
      });
    }
  });
});
