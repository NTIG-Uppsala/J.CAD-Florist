// "now" is already defined in the main script

// Function to sort the closed days
const sortClosedDays = () => {
    // Get the container of the closed days
    const closedDays = document.querySelector("#closed-days-container");

    // Get the current date in the format "MMDD"
    const currentDate = now.getMonth().toString().padStart(2, "0") + now.getDate().toString().padStart(2, "0");

    // Iterate through the two columns of closed days
    Array.from(closedDays.children).forEach((div) => {
        const childrenArray = Array.from(div.children);

        // Sort the closed days in an array based on the date attribute in ascending order
        childrenArray.sort((a, b) => {
            return a.dataset.date - b.dataset.date;
        });

        // Split the children based on the current date, creating two arrays
        const isAfterArray = childrenArray.filter((p) => p.dataset.date >= currentDate);
        const isBeforeArray = childrenArray.filter((p) => p.dataset.date < currentDate);

        // Concatenate the two arrays and append them to the div
        const sortedArray = isAfterArray.concat(isBeforeArray);
        div.innerHTML = "";
        sortedArray.forEach((p) => div.appendChild(p));
    });
};

// Sort the closed days
sortClosedDays();
