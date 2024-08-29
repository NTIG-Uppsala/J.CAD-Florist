let currentIndex = 0;

function moveCarousel(direction) {
    const track = document.querySelector('.carousel-track');
    const items = document.querySelectorAll('.carousel-item');
    const totalItems = items.length;
    const itemsToShow = 3; // visar 3 items
    const originalItemsCount = totalItems - itemsToShow; // exkludera klonade items
    const itemWidth = items[0].offsetWidth + parseFloat(getComputedStyle(items[0]).marginLeft) + parseFloat(getComputedStyle(items[0]).marginRight);

    currentIndex += direction;

    // loopa tillbaka
    if (currentIndex < 0) {
        currentIndex = originalItemsCount;
        track.style.transition = 'none'; // stäng av transition
        const newTransform = -currentIndex * itemWidth;
        track.style.transform = `translateX(${newTransform}px)`;
        setTimeout(() => {
            track.style.transition = 'transform 0.5s ease-in-out'; // aktivera transition
            currentIndex -= 1; // flytta tillbaka ett steg
            moveCarousel(0); // anropa moveCarousel med 0 för att uppdatera positionen
        }, 50);
        return;
    } else if (currentIndex >= originalItemsCount) {
        track.style.transition = 'transform 0.5s ease-in-out';
        const newTransform = -currentIndex * itemWidth;
        track.style.transform = `translateX(${newTransform}px)`;

        // reseta till första item efter att ha nått slutet
        setTimeout(() => {
            track.style.transition = 'none';
            currentIndex = 0; 
            track.style.transform = `translateX(0px)`;
            setTimeout(() => {
                track.style.transition = 'transform 0.5s ease-in-out';
            }, 50);
        }, 500);
        return;
    }

    const newTransform = -currentIndex * itemWidth;
    track.style.transform = `translateX(${newTransform}px)`;
}

// klona första items och lägg till dem i slutet
window.onload = function() {
    const track = document.querySelector('.carousel-track');
    const items = document.querySelectorAll('.carousel-item');
    const itemsToShow = 3; // Show only 3 items

    
    for (let i = 0; i < itemsToShow; i++) {
        const clone = items[i].cloneNode(true);
        track.appendChild(clone);
    }
};
