const sharp = require("sharp");
const fs = require("fs");
const path = require("path");

const imageFolder = "images/";
const assetFolder = "assets/images/";

const landscapeResolutions = [
    { width: 2560, height: 1440, path: path.join(imageFolder, "2560x1440/") },
    { width: 1920, height: 1080, path: path.join(imageFolder, "1920x1080/") },
    { width: 1600, height: 900, path: path.join(imageFolder, "1600x900/") },
    { width: 1536, height: 864, path: path.join(imageFolder, "1536x864/") },
    { width: 1440, height: 900, path: path.join(imageFolder, "1440x900/") },
    { width: 1366, height: 768, path: path.join(imageFolder, "1366x768/") },
    { width: 1280, height: 720, path: path.join(imageFolder, "1280x720/") },
];

const portraitResolutions = [
    { width: 412, height: 915, path: path.join(imageFolder, "412x915/") },
    { width: 393, height: 873, path: path.join(imageFolder, "393x873/") },
    { width: 393, height: 851, path: path.join(imageFolder, "393x851/") },
    { width: 390, height: 844, path: path.join(imageFolder, "390x844/") },
    { width: 360, height: 800, path: path.join(imageFolder, "360x800/") },
    { width: 375, height: 667, path: path.join(imageFolder, "375x667/") },
];

const ensureDirectoryExistence = (dir) => {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
};

fs.readdir(assetFolder, (err, files) => {
    if (err) {
        console.error("Error reading the asset folder:", err);
        return;
    }

    files.forEach((file) => {
        const image = sharp(path.join(assetFolder, file));

        [...landscapeResolutions, ...portraitResolutions].forEach((resolution) => {
            ensureDirectoryExistence(resolution.path);

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
