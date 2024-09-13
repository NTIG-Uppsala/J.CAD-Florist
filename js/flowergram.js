<<<<<<< HEAD
//Visar blommogrammet om man kallar funktionen
<<<<<<< HEAD:js/flower-gram.js
function flowergramBtnPressed() {
    let flowergramPopUp = document.getElementById('flowergram');
    flowergramPopUp.classList.toggle('show');
=======
=======
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
const checkZIPCode = () => {
    // Get the value from the input field and remove all non-digit characters
    const zip = inputField.value.replace(/\D/g, "");

    // List of valid ZIP codes
    const zipCodes = ["98138", "98140", "98141", "98144", "98145", "98146", "98147"];

    // Check if the user has entered a ZIP code
    if (zip === "") {
        writeOutput("Du måste skriva in ett postnummer!", "red");
        return;
    }

    // Check if the ZIP code is 5 digits long
    if (zip.length !== 5) {
        writeOutput("Postnumret måste vara 5 siffror!", "red");
        return;
    }

    // Check if the ZIP code is valid
    if (!zipCodes.includes(zip)) {
        writeOutput("Vi levererar tyvärr inte till detta postnummer!", "red");
        return;
    }
    writeOutput("Vi levererar till detta postnummer!", "green");
};

// Adds event listeners to the input field and button

inputButton.addEventListener("click", checkZIPCode);

inputField.addEventListener("blur", checkZIPCode);

inputField.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        checkZIPCode();
    }
});

// Function to toggle the flowergram popup
>>>>>>> 40aa214 (Skrev färdigt blommogramkoden och skrev kommenterar för allt)
const flowerGramPopUp = () => {
    const flowerGramPopUp = document.querySelector("#flowerGram");
    flowerGramPopUp.classList.toggle("show");
<<<<<<< HEAD
>>>>>>> 8e3c501 (Påbörjat omskrivning av postnummerscheck):js/flowerGram.js
}
=======
};
>>>>>>> 40aa214 (Skrev färdigt blommogramkoden och skrev kommenterar för allt)

// Adds event listener to the button
popupButton.addEventListener("click", flowerGramPopUp);
