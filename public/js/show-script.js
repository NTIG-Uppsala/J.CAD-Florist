// Loops through all elements with the class "script" and sets their display to block
// The class is used on elements that are not functional without JavaScript enabled
document.querySelectorAll(".script").forEach((script) => {
    script.style = "display: block;";
});
