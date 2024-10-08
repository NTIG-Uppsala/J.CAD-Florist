// Function to update the text field with the current status
const updateDynamicInformationStatus = () => {
    // Get the output text field
    const outputTextField = document.querySelector("#dynamic-information");

    // Get the current day, date, hour, minute, month and the opening hours for the current day
    const currentDate = now.getDate();
    const weekDay = now.getDay();
    const currentMonth = now.getMonth();

    // Check if the store is closed for a holiday and hide the banner if it is
    if (closedDays[currentMonth].includes(currentDate)) {
        hideBanner();
        return;
    }

    // Hide the banner if there are no deals of the day
    if (dealsOfTheDay[weekDay].length === 0) {
        hideBanner();
        return;
    }

    // Check if there is a deal of the day and add it to the output text field
    dealsOfTheDay[weekDay].forEach((deal) => {
        // Check if this day has a deal
        if (deal.id) {
            const product = document.querySelector(deal.id); // Get the product that has a deal
            const productName = product.querySelector("h4").textContent.toLowerCase(); // Get the name of the product
            const productPrice = deal.price; // Get the deal-price of the product
            const productOriginalPrice = product.querySelector(".original-price").textContent; // Get the original price of the product
            const output = data.lang.dealOfTheDayTextBanner.replace("{ productName }", productName).replace("{ productPrice }", productPrice).replace("{ productOldPrice }", productOriginalPrice); // Create the output text
            outputTextField.innerHTML = output; // Show the deal on the top of the page
        }
    });
};

const hideBanner = () => {
    const outputTextField = document.querySelector("#dynamic-information");
    outputTextField.parentElement.style.display = "none";
    return;
}

const showBanner = () => {
    const outputTextField = document.querySelector("#dynamic-information");
    outputTextField.parentElement.style.display = "block";
    return;
}

// Update the current status
updateDynamicInformationStatus();
