// Import the required modules
const fs = require("fs"); // File system module
const yaml = require("js-yaml"); // Module for converting YAML to JS-Objects
const handlebars = require("handlebars"); // Handlebars module

const helpers = require("../helpers/handlebars");

handlebars.registerHelper("translate", helpers.translate);

// Define the paths to the files and folders used when compiling the Handlebars template
const templateFile = "templates/index.hbs"; // Path to the Handlebars template file
const dataFolder = "data/data/"; // Path to a data folder where all the data files will be stored
const dataLangFolder = "data/data-lang/"; // Path to a data folder where all the language data files will be stored
const outputFolder = "public/"; // Path to the output folder
const jsFile = "js/data.js"; // Path to tje output js file for all the data

// Function to convert JS object to a string without quotes around keys
const objectToString = (obj) => {
    return JSON.stringify(obj, null, 2).replace(/"([^"]+)":/g, "$1:"); // Remove quotes around object keys
};

// Create the output folders if they don't exist
if (!fs.existsSync(outputFolder)) {
    fs.mkdirSync(outputFolder, { recursive: true });
}

// Convert YAML to JS-Object

const dataObj = {}; // Initialize an empty object to store the data
fs.readdirSync(`${dataFolder}/`).forEach((file) => {
    const fileContents = fs.readFileSync(`${dataFolder}/${file}`, "utf8");
    const data = yaml.load(fileContents);
    const [dataFile] = file.split("."); // Extract the location from the file name
    dataObj[dataFile] = data;
});

const dataLangObj = {}; // Initialize an empty object to store the language-data
fs.readdirSync(`${dataLangFolder}/`).forEach((file) => {
    const fileContents = fs.readFileSync(`${dataLangFolder}/${file}`, "utf8");
    const dataLang = yaml.load(fileContents);
    const [dataLangFile] = file.split("."); // Extract the location from the file name
    dataLangObj[dataLangFile] = dataLang;
});

const allLocalizationData = {};

// Create a function to compile the Handlebars template to HTML
const templateContents = fs.readFileSync(templateFile, "utf8");
const template = handlebars.compile(templateContents); // Correctly use the Handlebars instance

// Compile the html file
Object.keys(dataObj).forEach((dataFile) => {
    Object.keys(dataLangObj).forEach((dataLangFile) => {
        // Combine the data from the universal data files and the language data files
        const combinedData = {
            data: dataObj[dataFile],
            lang: dataLangObj[dataLangFile],
        };

        allLocalizationData[dataLangFile] = combinedData;

        // Generate the HTML output for the combined data
        const outputHtml = template(combinedData);

        // Define the output directory for the compiled HTML
        const combinedOutputFolder = `${outputFolder}${dataLangFile}/`; // Path to the output folder

        // Create the output folders if they don't exist
        if (!fs.existsSync(combinedOutputFolder)) {
            fs.mkdirSync(combinedOutputFolder, { recursive: true });
        }

        const outputFile = `${combinedOutputFolder}index.html`; // Path to the output file

        // Write the compiled HTML to the output file
        fs.writeFileSync(outputFile, outputHtml); // Write the output to the file

        console.log(`Generated ${outputFile}`);
    });
});

const jsData = `
const lang = document.querySelector("#data").dataset.lang;
const data = ${objectToString(allLocalizationData)}[lang];
`;

fs.writeFileSync(`${jsFile}`, jsData);

console.log(`Generated ${jsFile}`);
