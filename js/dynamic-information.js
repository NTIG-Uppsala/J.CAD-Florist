// List of closed days
// month: [days]

// get closed days from html

// Function to update the text field with the current status
const updateDynamicInformationStatus = () => {
    // Get the output text field
    const outputTextField = document.querySelector("#dynamic-information");
    console.log(outputTextField.parentElement);

    // Get the current day, date, hour, minute, month and the opening hours for the current day
    const currentDate = now.getDate();
    const currentMonth = now.getMonth();

    // Check if the store is closed for a holiday
    if (closedDays[currentMonth].includes(currentDate)) {
        // outputTextField.parentElement.style.display = "none";
        // document.documentElement.style.setProperty("--body-height", "var(--body-height-orignal)");
        // document.documentElement.style.setProperty("--body-responsive-height", "var(--body-responsive-height-original)");
        return;
    }
};

// Update the current status
updateDynamicInformationStatus();
