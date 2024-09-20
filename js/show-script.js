// Loops through all elements with the class "script" and sets their visibility to "visible"
// The class is used on elements that are not functional without JavaScript enabled
document.querySelectorAll(".script").forEach((script) => {
    script.style.visibility = "visible";
});
