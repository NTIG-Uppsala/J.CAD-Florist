// Initialize previous scroll position and get header element and its height 
let prevScrollPos = window.scrollY;
const header = document.querySelector("header");
const headerHeight = header.offsetHeight;

// Initialize state variables for mouse and scroll interactions
let isMouseNearHeader = false;
let isMouseInsideHeader = false;
let hasInteractedWithHeader = false;
let isScrolling = false;

// Throttle function to limit the rate at which a function can fire to improve performance
const throttle = (fn, wait) => {
    let isThrottled = false;
    return (...args) => {
        if (!isThrottled) {
            fn.apply(this, args);
            isThrottled = true;
            setTimeout(() => isThrottled = false, wait);
        }
    };
};

// Handle scroll event to show or hide the header based on scroll direction
const handleScroll = () => {
    const currentScrollPos = window.scrollY;

    // Only update header visibility if mouse is not interacting with the header
    if (!isMouseInsideHeader && !isMouseNearHeader && !hasInteractedWithHeader) {
        // Always show header if the scroll position is within one header height from the top
        if (currentScrollPos <= headerHeight) {
            header.style.top = "0"; // Always show the header at the top of the page
        } else if (prevScrollPos > currentScrollPos) {
            header.style.top = "0"; // Show header when scrolling up
        } else {
            header.style.top = `-${headerHeight}px`; // Hide header when scrolling down
        }
    }
    prevScrollPos = currentScrollPos; // Update previous scroll position
};

// Handle mouse move event to show header when mouse is near the top of the page
const handleMouseMove = throttle((event) => {
    const currentScrollPos = window.scrollY;
    const isNearTop = event.clientY <= headerHeight;

    if (isNearTop && !hasInteractedWithHeader) {
        isMouseNearHeader = true;
        header.style.top = "0"; // Show header
    } else {
        isMouseNearHeader = false;
        if (!isMouseInsideHeader && hasInteractedWithHeader && currentScrollPos > headerHeight) {
            header.style.top = `-${headerHeight}px`; // Hide header only if not at the top of the page
        }
    }
}, 100);

// Handle mouse enter event to show header when mouse enters the header
const handleMouseEnter = () => {
    isMouseInsideHeader = true;
    hasInteractedWithHeader = true;
    header.style.top = "0"; // Show header
};

// Handle mouse leave event to hide header when mouse leaves the header
const handleMouseLeave = () => {
    const currentScrollPos = window.scrollY;
    isMouseInsideHeader = false;
    // Do not hide header if at the top of the page
    if (!isMouseNearHeader && hasInteractedWithHeader && currentScrollPos > headerHeight) {
        header.style.top = `-${headerHeight}px`; // Hide header only if not at the top of the page
    }
    hasInteractedWithHeader = false;
};

// Add event listeners for scroll and mouse move events
window.addEventListener('scroll', throttle(() => {
    isScrolling = true;
    handleScroll();
    isScrolling = false;
}, 100));

window.addEventListener('mousemove', handleMouseMove);

// Add event listeners for mouse enter and leave events on the header
header.addEventListener('mouseenter', handleMouseEnter);
header.addEventListener('mouseleave', handleMouseLeave);
