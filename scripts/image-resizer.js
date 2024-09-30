const sharp = require("sharp");
const fs = require("fs");
const path = require("path");

// Ensure the directory exists and create it if it doesn't
const ensureDirectoryExistence = (dir) => {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
};

// Resize the images
const imageResizer = (folder, resolutions) => {
    // Read the folder
    fs.readdir(folder, (err, files) => {
        if (err) {
            console.error(`Error reading the folder ${folder}:`, err);
            return;
        }

        // Loop through the images
        files.forEach((file) => {
            const image = sharp(path.join(folder, file));

            // Loop through the resolutions
            resolutions.forEach((resolution) => {
                ensureDirectoryExistence(resolution.path);

                // Resize the image
                image.resize(resolution.width, resolution.height).toFile(path.join(resolution.path, file), (err, info) => {
                    if (err) {
                        console.error(`Error resizing the image ${file} to ${resolution.width}x${resolution.height}:`, err);
                    } else {
                        console.log(`Image resized: ${file} to ${resolution.width}x${resolution.height}`, info);
                    }
                });
            });
        });
    });
};

// Output folder
const imageFolder = "images/";

// Slideshow images
const slideshowFolder = "assets/images/slideshow/";

// Slideshow resolutions
const slideshowLandscapeResolutions = [
    { width: 2560, height: 1440, path: path.join(imageFolder, "2560x1440/") },
    { width: 1920, height: 1080, path: path.join(imageFolder, "1920x1080/") },
    { width: 1600, height: 900, path: path.join(imageFolder, "1600x900/") },
    { width: 1536, height: 864, path: path.join(imageFolder, "1536x864/") },
    { width: 1440, height: 900, path: path.join(imageFolder, "1440x900/") },
    { width: 1366, height: 768, path: path.join(imageFolder, "1366x768/") },
    { width: 1280, height: 720, path: path.join(imageFolder, "1280x720/") },
];

const slideshowPortraitResolutions = [
    { width: 1440, height: 1024, path: path.join(imageFolder, "1440x1024/") },
    { width: 1080, height: 768, path: path.join(imageFolder, "1080x768/") },
    { width: 412, height: 915, path: path.join(imageFolder, "412x915/") },
    { width: 393, height: 873, path: path.join(imageFolder, "393x873/") },
    { width: 393, height: 851, path: path.join(imageFolder, "393x851/") },
    { width: 390, height: 844, path: path.join(imageFolder, "390x844/") },
    { width: 360, height: 800, path: path.join(imageFolder, "360x800/") },
    { width: 375, height: 667, path: path.join(imageFolder, "375x667/") },
];

// Resize the slideshow images
imageResizer(slideshowFolder, [...slideshowLandscapeResolutions, ...slideshowPortraitResolutions]);

// Product images
const productFolder = "assets/images/products/";

// Product resolutions
const productResolutions = [
    { width: 480, height: 320, path: path.join(imageFolder, "480x320/") },
    { width: 384, height: 256, path: path.join(imageFolder, "384x256/") },
    { width: 320, height: 213, path: path.join(imageFolder, "320x213/") },
    { width: 256, height: 170, path: path.join(imageFolder, "256x170/") },
    { width: 224, height: 149, path: path.join(imageFolder, "224x149/") },
];

// Resize the product images
imageResizer(productFolder, productResolutions);

// Employee images
const employeeFolder = "assets/images/employees/";

// Employee resolutions
const employeeResolutions = [{ width: 272, height: 408, path: path.join(imageFolder, "272x408/") }];

// Resize the employee images
imageResizer(employeeFolder, employeeResolutions);
