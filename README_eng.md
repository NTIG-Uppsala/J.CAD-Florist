# Florista

Florista is a website created for a florist company by the TE4 group J.CAD.

Members: Axel Thornberg, Jesper Cejie, Eskil Tornberg.

[Link to the website](https://ntig-uppsala.github.io/J.CAD-Florist/)

---

## Project Standards 

[Development Environment](docs/development-environment-standard.md)

[Code Analysis](docs/code-analysis.md)

[Programming Language](docs/programming-language-standard.md)

[Coding Standards](docs/coding-standard.md)

---

## Guides

[Collection of guides for the website](docs/guides.md)

---

## Flask
The website is built using the Flask web framework.

### Python Virtual Environment
To run the website, all dependencis need to be installed.
First, create a python virtual environment to containerize an installation.

``python -m venv venv``

To enter the created virtual environment if you are on windows, run:

``venv\Scripts\activate``

or if you are on macOS or Linux, run:

``source venv/bin/activate``

### Install dependencies

After having created and entered the python virtual environment, you can install the necessary dependencies to be able to run the flask application.
The file [requirements.txt](requirements.txt) contains the python packages necessary for the project.
To install the packages, run the following in the root directory of the project:

``pip install -r requirements.txt``

### Run Development Website
To start a development Flask server for the website, run:

``flask run``

This will start the server on a specfic port, which is printed on the console.
To change the port that the server runs on, edit the value of `FLASK_RUN_PORT` in the [.flaskenv](.flaskenv) file.

---

## Website Content Tests

The project uses tests to verify the content of the website. The various test files are located in the [tests](https://github.com/NTIG-Uppsala/J.CAD-Florist/tree/main/tests) directory.
To run tests for the website, Python 3.12.5 is required, which can be installed at [python.org](https://www.python.org/downloads/release/python-3125/).

Then, open the project in a command prompt and run these commands:

```bash
pip install playwright lxml
```

```bash
python -m playwright install
```

To configure the tests, go to view --> testing --> configure python tests --> unittests --> tests.

There is also a Python script that generates screenshots of the website. This script can be run by typing `python .\tests\screenshots.py`.

---

## Image Resolutions

This page uses a script to create variations of images in different resolutions to optimize loading times. For this, [Node.js](https://nodejs.org/en) is required.

Once Node.js is installed, the following command should be run in the project's root folder:
```bash
npm install
```
This will install all packages required to run the project.

If there is a need to create all images again (e.g., if new resolutions or images have been added), run the following command:
```bash
npm run resize
```

---

## Icons

Icons are taken from [icons8](https://icons8.com/) and [iconmonstr](https://iconmonstr.com/).

---

## How to Change Information on the Website:

Everything that follows must also be changed in the test files so that the information checked by the tests aligns with what should be checked.

### Products
The price of existing products is changed in the [data.yml](data/data/data.yml) file under the "Product Prices" comment.

New products are added under the "Products" comment. Make sure to follow the same formatting as the existing products.

Product images are also changed under the "Products" comment for each respective product.

Product names are changed in the respective language file in the [språkfilsmappen](data/data-lang/) under the "Products section" comment. Here you can also edit the alt text for the images.

### Company Information
Company information, such as the company name, address, or contact details, is changed in [data.yml](data/data/data.yml) under the "Company Information" comment.

For the map, there is a link in `companyMapSource` in [data.yml](data/data/data.yml) under the "Company Information" comment that also needs to be changed.

### Opening Hours

Opening hours are changed in the [data.yml](data/data/data.yml) file under the "Opening Hours" comment.

### Closed Days
Information about closed days is changed in the respective language file in the [language file folder](data/data-lang/) under the "Closed days" comment.

### Delivery Zip Codes 
To change which zip codes are delivered to, modify the list `zipCodes` in [flowergram.js](public/js/flowergram.js).

### Staff Information
Staff information is changed in the respective language file in the [language file folder](data/data-lang/) under the "Employee information section" comment.

### Deals of the Day
To change the deals of the day, the object `dealsOfTheDay` in [deal-of-the-day.js](public/js/deal-of-the-day.js) should be modified. The object has 7 keys, one for each day where Sunday is day 0 and Saturday is day 6. The values of these keys are lists of objects where each object is a deal. Each deal has two keys and two values: `price` determines the new price and `id` determines the product ID. Change the values of these keys if existing deals need to be modified. To add new deals, create new objects that follow the same structure in the list corresponding to the day the deal should apply.

### Information Message
To change what is displayed in the information message, modify `outputTextField.innerHTM` in [dynamic-information.js](public/js/dynamic-information.js).