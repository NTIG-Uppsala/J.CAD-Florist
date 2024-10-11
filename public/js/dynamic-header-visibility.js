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
        if (prevScrollPos > currentScrollPos) {
            header.style.top = "0"; // Show header
        } else {
            header.style.top = `-${headerHeight}px`; // Hide header
        }
    }
    prevScrollPos = currentScrollPos; // Update previous scroll position
};

// Handle mouse move event to show header when mouse is near the top of the page
const handleMouseMove = throttle((event) => {
    const isNearTop = event.clientY <= headerHeight;

    if (isNearTop && !hasInteractedWithHeader) {
        isMouseNearHeader = true;
        header.style.top = "0"; // Show header
    } else {
        isMouseNearHeader = false;
        if (!isMouseInsideHeader && hasInteractedWithHeader) {
            header.style.top = `-${headerHeight}px`; // Hide header
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
    isMouseInsideHeader = false;
    if (!isMouseNearHeader && hasInteractedWithHeader) {
        header.style.top = `-${headerHeight}px`; // Hide header
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