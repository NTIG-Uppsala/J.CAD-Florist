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

## Icons

Icons are taken from [icons8](https://icons8.com/) and [iconmonstr](https://iconmonstr.com/).

---

## Configuration of GitHub Pages

In this project, GitHub Pages is used as a staging area to easily present completed features to the customer. Pages are also used to easily test parts of the website on different devices.

1. Log in to github.com.
2. Open the J.CAD-FLORIST repository.
3. Navigate to "Settings."
4. Select the "Pages" tab under "Code and automation."
5. Ensure that "Source" under "Build and deployment" is set to "Deploy from a branch."
6. Under "Branch," select "live" and "/ (root)."
7. Then click "Save."

---

## Update GitHub Pages Site

Github Pages is built from the `live` branch.
All completed changes should be pushed to the `main` branch. 
When a feature is fully finished, it should be merged or rebased into the `live` branch.

---

## Web Server
### How to Access the Web Server

The web server is used to publish features that the product owner has approved as fully complete so they can be used by the customer.

1. Open a command prompt and type:
```bash
ssh root@<ip> -p <port>
```
2. Type `yes` if prompted.
3. When prompted, enter the password.
4. Navigate to the correct directory:
```bash
cd /var/www/html
```
5. If the directory is empty:
```bash
git clone https://github.com/NTIG-Uppsala/J.CAD-Florist .
```
6. Switch to the latest release:
```bash
git checkout <your tag>
```

---

### How to Release a New Version

Open a command prompt and type:

```bash
git fetch
git checkout <your tag>
```

If you're unsure, list all tags by typing:

```bash
git tag
```

## Installing and Running Flask
The website backend is built with the Flask web framework.

### Python Virtual Environment
To run the website, all dependencies for it need to be installed.
This can be done through a python virtual environment, which ensures that all python packages that are installed via `pip` will be containerized inside of the virtual environment, instead of globally on the system.
First, create a python virtual environment:

``python -m venv venv``

To source and enter the created virtual environment if you are on windows, run:

``venv\Scripts\activate``

or if you are on macOS, Linux, or another unix-based operating system, run:

``source venv/bin/activate``

Once having sourced the virtual environment, `(venv)` will appear to the left of your prompt on the command line.
To exit the virtual environment, simply run `exit` on the command line.

### Install Dependencies

After having created and entered the python virtual environment, you can install the necessary dependencies to be able to run the Flask application.
The file [requirements.txt](requirements.txt) contains the python packages necessary for the project.
To install the packages, run the following in the root directory of the project:

``pip install -r requirements.txt``

### Update Dependencies

After installing additional packages for the project, ensure that requirements.txt is updated by running:

``pip freeze > requirements.txt``

### Run Development Server
To start a development Flask server for the website, run:

``flask run``

This will start the server on a specific port, which is then printed on the console.
To change the port that the server runs on, edit the value of `FLASK_RUN_PORT` in the [.flaskenv](.flaskenv) file.

---

## Overview of the Flask Application
The python file `florista.py` located in the root directory is the main file that is executed when running `flask run`, and in turn imports everything from the `app/` directory.
The `app/` directory contains all the files and directories which the website uses, which is treated by Flask as a python package when imported.
This is due to the `__init__.py` located in it, which initializes the `app` package and configures various things at startup.

Inside of the `app/` directory are various files directories which perform different functions for the website.

### Routes and Templates
`routes.py` describes the routes for the website.
It contains functions which are interpreted and return at different routes, or pathways of the website.
This can be static or template HTML files, but also for instance files or redirects to other functions inside of `routes.py`.
The `@app.route` decorators set before the function definitions specify pathways for the site where the functions will be interpreted.
For instance, setting `@app.route('/index')` before a function will set the function to be interpreted after navigating to `<url-of-site>/index` in your browser.
Setting `@app.route('/')` before a function will set it as the default function to run when entering the root url of the site.
Multiple `@app.route` decorators can be set before a function definition.

The `templates/` directory contains the template HTML files used for the website.
Templates can contain placeholders for dynamic information which gets sent from the Flask server.
[Jinja](https://jinja.palletsprojects.com/en/3.1.x/) is the templating engine used for this project.
It can process variables sent via Flask to the templates, which are sent in the return statements of the functions in `routes.py`.
Following is an example function:

```
@app.route('/en')
def en():
    lang = "en"
    return render_template('index.html', lang=lang)
```

The above functíon will render the file `index.html` located at `templates/` and send the variable `lang` into `index.html` where it can be processed through Jinja.
Putting `{{ lang }}` inside of the HTML file will replace that with the variable value when the page is rendered, in this case with "en".

The file `base.html` in `templates/` is used to create a base structure to include in other template files.
`{% extends "base.html" %}` is included at the top of every new template file to define `base.html` as the master template that the template inherits from.
`{% block content %}{% endblock %}` is set inside of `base.html` to define where the content of the template files should be put inside of `base.html`.
All the content within the template files then have to be defined as:

```
{% block content %}
<content>
{% endblock %}
```

where `<content>` is replaced with the actual HTML content.

### Database
The project uses an sqlite database, which is handled through the SQLAlchemy python package.

`models.py` describes models used to create tables for the database.
It consists of class definitions that act as schemas for creating database tables.

### Static

The `static/` directory contains various subdirectories containing static files used for the website.
`static/css/` contains the various CSS files used for styling of the website.
`static/js/` contains the JavaScript files used for frontend scripting on the website.
`static/images/` contains all the images which are used on the website.

### Miscellaneous

`config.py` sets various configurations used by the Flask application.
It defines the class `Config` which contains variables used by Flask.

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

Once Node.js is installed, the following command should be run in the project's root directory:
```bash
npm install
```
This will install all packages required to run the project.

If there is a need to create all images again (e.g., if new resolutions or images have been added), run the following command:
```bash
npm run resize
```

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
Information about closed days is changed in the respective language file in the [language file directory](data/data-lang/) under the "Closed days" comment.

### Delivery Zip Codes
To change which zip codes are delivered to, modify the list `zipCodes` in [flowergram.js](public/js/flowergram.js).

### Staff Information
Staff information is changed in the respective language file in the [language file directory](data/data-lang/) under the "Employee information section" comment.

### Deals of the Day
To change the deals of the day, the object `dealsOfTheDay` in [deal-of-the-day.js](public/js/deal-of-the-day.js) should be modified. The object has 7 keys, one for each day where Sunday is day 0 and Saturday is day 6. The values of these keys are lists of objects where each object is a deal. Each deal has two keys and two values: `price` determines the new price and `id` determines the product ID. Change the values of these keys if existing deals need to be modified. To add new deals, create new objects that follow the same structure in the list corresponding to the day the deal should apply.

### Information Message
To change what is displayed in the information message, modify `outputTextField.innerHTML` in [dynamic-information.js](public/js/dynamic-information.js).