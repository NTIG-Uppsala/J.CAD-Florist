// Object for the deals of the day with the day of the week as key and an array of objects for each deal with the price and the id of the product as value
const dealsOfTheDay = {
    0: [],
    1: [{ price: "89 kr", id: "#product-tulpaner-10-pack" }],
    2: [{ price: "19 kr/st", id: "#product-liljor" }],
    3: [{ price: "39 kr", id: "#product-hortensia" }],
    4: [{ price: "79 kr", id: "#product-aloe-vera" }],
    5: [{ price: "79 kr", id: "#product-kaktus-i-kruka" }],
    6: [{ price: "127 kr", id: "#product-rosor-10-pack" }],
};

// Function to set the deal of the day
const setDealOfTheDay = () => {
    // Get the current day of the week
    const weekDay = now.getDay();

    // Get all products with an active deal of the day
    const activeProducts = document.querySelectorAll(".product:has(.active)");

    // Remove any existing active deals of the day (Should not apply to users, but is necessary for testing as well as beneficial for development and as a fail-safe)
    activeProducts.forEach((product) => {
        product.querySelector(".active").classList.remove("active");
        product.querySelector(".new-price").classList.remove("new-price");
        product.querySelector(".original-price").remove();
    });

    // Set the deals of the day
    dealsOfTheDay[weekDay].forEach((deal) => {
        // Get the product that has a deal
        const product = document.querySelector(deal.id);

        // Turn the old price gray and dash-through it
        product.querySelector("h5").classList.add("original-price");

        // Create a new price element, style it, and set the new price
        const newPrice = document.createElement("h5");
        newPrice.classList.add("new-price");
        newPrice.classList.add("price");
        newPrice.textContent = deal.price;

        // Insert the new price before the old price and make the product active to unhide the "Dagens klipp" text
        product.querySelector(".original-price").before(newPrice);
        product.querySelector("p").classList.add("active");
    });

    const products = document.querySelectorAll(".product");

    // Move the products with a deal of the day to the top of the product list
    products.forEach((product) => {
        if (product.querySelector(".active")) {
            document.querySelector("#product-container").prepend(product);
        }
    });
};

// Call the function to set the deal of the day
setDealOfTheDay();
