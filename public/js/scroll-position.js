const dropdownItems = document.querySelectorAll('.dropdown-item');

// Store the scroll position when a dropdown item is clicked
dropdownItems.forEach((item) => {
    item.addEventListener('click', (event) => {
        sessionStorage.setItem('scrollPosition', window.scrollY);
    });
});

// Restore the scroll position when the page loads
window.addEventListener('load', () => {
    const scrollPosition = sessionStorage.getItem('scrollPosition');
    if (scrollPosition !== null) {
        window.scrollTo(0, parseInt(scrollPosition, 10));
    }
});