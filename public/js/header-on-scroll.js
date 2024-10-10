// Define variables
let prevScrollpos = window.scrollY;
const header = document.getElementsByTagName("header")[0];
const headerHeight = header.clientHeight;

// Event listener to hide the header on scroll down and show it on scroll up
window.addEventListener('scroll', () => {
    const currentScrollPos = window.scrollY;
    if (prevScrollpos > currentScrollPos) {
        header.style.top = "0";
    } else {
        header.style.top = `-${headerHeight}px`;
    }
    prevScrollpos = currentScrollPos;
});