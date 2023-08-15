document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("contact-form");

    contactForm.addEventListener("submit", function (event) {
        event.preventDefault();
        alert("Form submitted! Thank you for contacting me.");
        contactForm.reset();
    });
});