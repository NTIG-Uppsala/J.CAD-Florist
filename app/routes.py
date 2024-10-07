from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/se')
def index():
    return render_template('index.html')

# Istället för handlebars har en index fil som en template som ändrar språk beroende på vilken route som används


# @app.route('/en')
# def en():
#     return render_template('en/index.html')

# @app.route('/se')
# def se():
#     return render_template('se/index.html')

# @app.route('/no')
# def no():
#     return render_template('no/index.html')