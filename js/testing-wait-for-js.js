// Adds a hidden div to the body element with the id JSLoaded to indicate that the JavaScript has loaded. This is used in the testing to ensure that all JavaScript has executed before running the tests.

const JSLoaded = document.createElement("div");
JSLoaded.setAttribute("hidden", "true");
JSLoaded.setAttribute("id", "JSLoaded");
document.body.appendChild(JSLoaded);
