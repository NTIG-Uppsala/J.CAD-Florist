// This file is ran by github workflows. There is no need to install any dependencies in this file or to run it manually.

const fs = require("fs");
const glob = require("glob");
const axios = require("axios");

// W3C Validation Service endpoint
const API_URL = "https://validator.w3.org/nu/";

// Get all HTML files in the repository
const files = glob.sync("**/*.html");

const validateFile = async (file) => {
    const content = fs.readFileSync(file, "utf8");
    try {
        const response = await axios.post(API_URL, content, {
            headers: {
                "Content-Type": "text/html; charset=utf-8",
                Accept: "application/json",
            },
        });
        return {
            file: file,
            results: response.data,
        };
    } catch (error) {
        return {
            file: file,
            error: error.response ? error.response.data : error.message,
        };
    }
};

const validateAllFiles = async () => {
    try {
        const validationResults = await Promise.all(files.map(validateFile));
        fs.writeFileSync("validation_results/validation_output.json", JSON.stringify(validationResults, null, 2));
    } catch (error) {
        console.error("Validation failed:", error);
        process.exit(1);
    }
};

validateAllFiles();
