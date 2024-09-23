// "now" is already defined in the main script

// Function to sort the closed days
const sortClosedDays = () => {
    // Get the container of the closed days
    const closedDays = document.querySelector("#closed-days-container");

    // Get the current date in the format "MMDD"
    const currentDate = now.getMonth().toString().padStart(2, "0") + now.getDate().toString().padStart(2, "0");

    Array.from(closedDays.children).forEach((div) => {
        // Sort the div based on the date before splitting it based on the current date
        const childrenArray = Array.from(div.children);
        childrenArray.sort((a, b) => {
            return a.dataset.date - b.dataset.date;
        });
        const isAfterArray = childrenArray.filter((p) => p.dataset.date >= currentDate);
        const isBeforeArray = childrenArray.filter((p) => p.dataset.date < currentDate);
        const sortedArray = isAfterArray.concat(isBeforeArray);
        div.innerHTML = "";
        sortedArray.forEach((p) => div.appendChild(p));
    });
};

// Update the current status
sortClosedDays();

now.setFullYear(2024, 11, 29);

sortClosedDays();
