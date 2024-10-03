popupButton = document.querySelector("#flowergram-btn");
inputField = document.querySelector("#postal-code");
inputButton = document.querySelector("#postal-code-btn");

// Helper function to write output to the user
const writeOutput = (message, color) => {
    const output = document.querySelector("#input-response");
    output.innerHTML = message;
    output.style.color = color;
    output.classList.remove("fade-in");
    void output.offsetWidth;
    output.classList.add("fade-in");
};

// Function to check if the ZIP code is valid
const checkZipCode = () => {
    // Get the value from the input field and remove all non-digit characters
    const zip = inputField.value.replace(/\D/g, "");

    // List of valid ZIP codes
    const zipCodes = ["98138", "98140", "98141", "98144", "98145", "98146", "98147"];

    // Check if the user has entered a ZIP code
    if (zip === "") {
        writeOutput(data.lang.noZipCode, "red");
        return;
    }

    // Check if the ZIP code is 5 digits long
    if (zip.length !== 5) {
        writeOutput(data.lang.zipCodeNotCorrectLength, "red");
        return;
    }

    // Check if the ZIP code is valid
    if (!zipCodes.includes(zip)) {
        writeOutput(data.lang.invalidZipCode, "red");
        return;
    }
    writeOutput(data.lang.validZipCode, "green");
};

// Adds event listeners to the input field and button

inputButton.addEventListener("click", checkZipCode);

inputField.addEventListener("blur", checkZipCode);

inputField.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        checkZipCode();
    }
});

// Function to toggle the flowergram popup
const flowerGramPopUp = () => {
    const flowerGramPopUp = document.querySelector("#flowergram");
    flowerGramPopUp.classList.toggle("show");
};

// Adds event listener to the button
popupButton.addEventListener("click", flowerGramPopUp);
