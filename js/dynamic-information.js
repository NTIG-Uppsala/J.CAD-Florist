// Function to update the text field with the current status
const updateDynamicInformationStatus = () => {
    // Get the output text field
    const outputTextField = document.querySelector("#dynamic-information");
    // console.log(outputTextField.parentElement);

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
        // Get the product that has a deal
        if (deal.id) {
            const product = document.querySelector(deal.id);
            const productName = deal.id.substr(deal.id.indexOf("-") + 1).replace(/-/g, " ");
            const productPrice = deal.price;
            const productOriginalPrice = product.querySelector(".original-price").textContent;
    
            outputTextField.innerHTML = `Idag kostar ${productName} endast ${productPrice} istället för ${productOriginalPrice}!`;
        }
    });
};

const hideBanner = () => {
    const outputTextField = document.querySelector("#dynamic-information");
    outputTextField.parentElement.style.display = "none";
    document.documentElement.style.setProperty("--body-height", "var(--body-height-orignal)");
    document.documentElement.style.setProperty("--body-responsive-height", "var(--body-responsive-height-original)");
    return;
}

const showBanner = () => {
    const outputTextField = document.querySelector("#dynamic-information");
    outputTextField.parentElement.style.display = "block";
    document.documentElement.style.setProperty("--body-height", "calc(var(--body-height-orignal) + var(--page-top-banner-height))");
    document.documentElement.style.setProperty("--body-responsive-height", "calc(var(--body-responsive-height-original) + var(--page-top-banner-height))");
    return;
}

// Update the current status
updateDynamicInformationStatus();
