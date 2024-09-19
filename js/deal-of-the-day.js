// const dealsOfTheDay = [ ... ]; all days that have deals, which products the deals apply to and what the deals are

// Get the current day, date

// Get the element of the product that is on sale today

// set the deal of the day-elements of the product to be visible/active
const dealsOfTheDay = {
    0: [],
    1: [{ price: "89 kr", id: "#product-tulpaner-10-pack" }],
    2: [{ price: "19 kr/st", id: "#product-liljor" }],
    3: [{ price: "39 kr", id: "#product-hortensia" }],
    4: [{ price: "79 kr", id: "#product-aloe-vera" }],
    5: [{ price: "79 kr", id: "#product-kaktus-i-kruka" }],
    6: [
        { price: "127 kr", id: "#product-rosor-10-pack" },
        { price: "99 kr", id: "#product-brollopsbukett" },
    ],
};

const setDealOfTheDay = () => {
    const weekDay = now.getDay();
    console.log(dealsOfTheDay[weekDay]);
    // Remove existing deals of the day
    const products = document.querySelectorAll(".product");
    products.forEach((product) => {
        if (product.querySelector(".active")) {
            product.querySelector(".active").classList.remove("active");
            const spans = product.querySelectorAll("span");
            spans[0].querySelector("h5").classList.remove("new-price");
            spans[1].remove();
        }
    });

    dealsOfTheDay[weekDay].forEach((deal) => {
        const product = document.querySelector(deal.id);
        const span = product.querySelector("span");
        span.querySelector("h5").classList.add("old-price");
        const newPriceSpan = document.createElement("span");
        const newPrice = document.createElement("h5");
        newPrice.classList.add("new-price");
        newPrice.classList.add("price");
        newPrice.textContent = deal.price;
        newPriceSpan.appendChild(newPrice);
        span.insertAdjacentElement("beforebegin", newPriceSpan);

        product.querySelector("p").classList.add("active");
    });

    console.log(document.querySelectorAll(".active").length);
};

setDealOfTheDay();
