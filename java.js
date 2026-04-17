function toggleMenu() {
  document.getElementById("mobileMenu").classList.toggle("open");
}
function closeMenu() {
  document.getElementById("mobileMenu").classList.remove("open");
}

// Scroll reveal
const revealEls = document.querySelectorAll(".reveal");
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add("visible");
      }
    });
  },
  { threshold: 0.1 },
);
revealEls.forEach((el) => observer.observe(el));

function handleBooking() {
  const name = document.querySelector('#booking input[type="text"]').value;
  const phone = document.querySelector('#booking input[type="tel"]').value;
  const service = document.querySelector('#booking select').value;
  const notes = document.querySelector('#booking textarea').value;

  if (!name || !phone) {
    alert("Please fill in your name and phone number to book virtual consultation/appointment.");
    return;
  }

  const message = `Hello Palak's Magic! ✦
  
I would like to book an appointment.

*Customer Details:*
- *Name:* ${name}
- *Phone:* ${phone}
- *Service:* ${service || 'Selection on chat'}

*Additional Info:*
${notes || 'None'}

Please let me know your availability!`;

  const whatsappNumber = "919555693813";
  const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;
  
  window.open(whatsappUrl, '_blank');
}

function handleContact() {
  const inputs = document.querySelectorAll(".cf-input");
  const msg = document.querySelector(".cf-textarea").value;
  if (!inputs[0].value || !inputs[1].value) {
    alert("Please fill in your name and phone number.");
    return;
  }
  alert(
    "✦ Message received! We'll get back to you at " +
      inputs[1].value +
      " soon.\n\nThank you for reaching out to Palak's Magic!",
  );
}

// Smooth nav active state
window.addEventListener("scroll", () => {
  const links = document.querySelectorAll(".nav-links a");
  const sections = document.querySelectorAll("section[id]");
  let current = "";
  sections.forEach((s) => {
    if (window.scrollY >= s.offsetTop - 80) current = s.getAttribute("id");
  });
  links.forEach((a) => {
    a.style.color =
      a.getAttribute("href") === "#" + current ? "var(--gold)" : "";
  });
});
