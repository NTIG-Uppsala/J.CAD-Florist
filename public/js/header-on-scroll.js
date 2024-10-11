let prevScrollpos = window.scrollY; // Get the current page offset
const header = document.getElementsByTagName("header")[0]; // Get the header element
const headerHeight = header.clientHeight; // Get the height of the header

window.addEventListener('scroll', () => { // When the user scrolls
    console.log('scrolling');
    const currentScrollPos = window.scrollY; // Get the current page offset
    if (prevScrollpos > currentScrollPos) { // If the previous offset is greater than the current offset
        header.style.top = "0"; // Show the header
    } else { // If the previous offset is less than the current offset
        header.style.top = `-${headerHeight}px`; // Hide the header
    }
    prevScrollpos = currentScrollPos; // Set the previous offset to the current offset
});

document.addEventListener('mouseover', (event) => {
    if (event.clientY <= headerHeight) { // Check if the mouse is within the height of the header
        header.style.top = "0"; // Show the header
    }
});
