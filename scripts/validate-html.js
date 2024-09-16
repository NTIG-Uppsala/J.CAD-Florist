// This file is ran by github workflows. There is no need to install any dependencies in this file or to run it manually.

const w3cjs = require("w3cjs");
const fs = require("fs");
const glob = require("glob");

// Get all HTML files in the repository
const files = glob.sync("**/*.html");

let validationResults = [];

files.forEach((file) => {
    w3cjs.validate({
        file: file,
        output: "json",
        callback: (err, res) => {
            if (err) {
                console.error("Validation error:", err);
            } else {
                validationResults.push({ file: file, results: res });
            }
        },
    });
});

// Save the results to a file
fs.writeFileSync("validation_results/validation_output.json", JSON.stringify(validationResults, null, 2));
