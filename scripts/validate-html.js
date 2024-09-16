const w3cjs = require("w3cjs");
const fs = require("fs");
const glob = require("glob");

// Get all HTML files in the repository
const files = glob.sync("**/*.html");

let validationResults = [];

const validateFile = (file) => {
    return new Promise((resolve, reject) => {
        w3cjs.validate({
            file: file,
            output: "json",
            callback: (err, res) => {
                if (err) {
                    reject({ file: file, error: err.message });
                } else {
                    resolve({ file: file, results: res });
                }
            },
        });
    });
};

const validateAllFiles = async () => {
    try {
        for (const file of files) {
            const result = await validateFile(file);
            validationResults.push(result);
        }
        fs.writeFileSync("validation_results/validation_output.json", JSON.stringify(validationResults, null, 2));
    } catch (error) {
        console.error("Validation failed:", error);
        process.exit(1);
    }
};

validateAllFiles();
