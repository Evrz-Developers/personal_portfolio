console.log("started!")
const toTopLink = document.getElementById('to_top');

// Add a click event listener to the link
toTopLink.addEventListener('click', () => {
  // Select the header section by its class name
  const headerSection = document.querySelector('.header');

  // Scroll to the header section
  headerSection.scrollIntoView({ behavior: 'smooth' });
});

const handleFirstTab = (e) => {
    if (e.key === 'Tab') {
        document.body.classList.add('user-is-tabbing')

        window.removeEventListener('keydown', handleFirstTab)
        window.addEventListener('mousedown', handleMouseDownOnce)
    }

}

const handleMouseDownOnce = () => {
    document.body.classList.remove('user-is-tabbing')

    window.removeEventListener('mousedown', handleMouseDownOnce)
    window.addEventListener('keydown', handleFirstTab)
}

window.addEventListener('keydown', handleFirstTab)

const backToTopButton = document.querySelector(".back-to-top");
let isBackToTopRendered = false;

let alterStyles = (isBackToTopRendered) => {
    backToTopButton.style.visibility = isBackToTopRendered ? "visible" : "hidden";
    backToTopButton.style.opacity = isBackToTopRendered ? 1 : 0;
    backToTopButton.style.transform = isBackToTopRendered
        ? "scale(1)"
        : "scale(0)";
};

window.addEventListener("scroll", () => {
    if (window.scrollY > 700) {
        isBackToTopRendered = true;
        alterStyles(isBackToTopRendered);
    } else {
        isBackToTopRendered = false;
        alterStyles(isBackToTopRendered);
    }
});
var typed = new Typed(".typing-text", {
    strings: ["Web-Apps", "Web-APIs", "Front-end", "Back-end.", "Python", "Django", "Django-REST", "Odoo Apps.", "HTML5, CSS3,", " Bootstrap 5", "JavaScript,", "Jquery", "R-DBMS.", "The UnExplored!"]
    ,
    loop: true,
    typeSpeed: 70,
    backSpeed: 10,
    backDelay: 500,
    startDelay: 1000, // wait for 1 second before starting the animation
    showCursor: true // show the cursor
});
