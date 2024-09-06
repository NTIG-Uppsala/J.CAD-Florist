//Visar blommogrammet om man kallar funktionen
function flowerGramPopUp() {
    var flowerGramPopUp = document.getElementById('flowerGram');
    flowerGramPopUp.classList.toggle('show');
}

//Lista av alla korrekta postnummer
const postalCodes = [
    "981 38",
    "981 40",
    "981 41",
    "981 44",
    "981 45",
    "981 46",
    "981 47",
]

function handleKeyDown(event) {
    //Om enter trycks så kör getPostalCode
    if (event.key === "Enter") {
        getPostalCode();
    }
    //Får värdet ifrån inputfältet
    let currentInput = document.getElementById("postalCode").value;

    //Förhindrar att användaren kan trycka space förutom efter de tre första siffrorna
    if (event.key === " " && currentInput.length !== 3) {
        event.preventDefault();
        return;
    }

    //Förhindrar att användaren kan skriva in något annat än siffror, backspace och space
    if (!/^[0-9]$/.test(event.key) && event.key !== 'Backspace' && event.key !== ' ' && event.key !== 'Enter') {
        event.preventDefault();
        return;
    }

    //om användaren glömmer trycka space efter de tre första siffrorna
    if (event.key !== "Backspace" && event.key !== " " && currentInput.length == 3) {
        document.getElementById("postalCode").value += " ";
    }  
}

//Funktion som kollar om postnumret finns i listan
function getPostalCode() {
    //Får värdet ifrån inputfältet
    var postalCodeInput = document.getElementById("postalCode").value;
    var inputResponse = document.getElementById("inputMessage");
    //Om postnumret finns i listan så skrivs detta ut
    if(postalCodes.includes(postalCodeInput)) {
        inputResponse.innerHTML = "Vi levererar till detta postnummer!";
        inputResponse.style.color = "green";
    //Om postnumret inte finns i listan så skrivs detta ut
    } else {
        inputResponse.innerHTML = "Vi levererar tyvärr inte till detta postnummer!";
        inputResponse.style.color = "red";
    }
}