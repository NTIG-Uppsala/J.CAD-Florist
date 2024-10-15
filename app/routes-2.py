from flask import render_template
from app import app

# Istället för handlebars har en index fil som en template som ändrar språk beroende på vilken route som används
# SKicka data vid route så att det kan användas av jinja i templates

@app.route('/')
@app.route('/se')
def se():
    lang = "sv"
    return render_template('index.html', lang=lang)

@app.route('/admin')
def admin():
    lang = "sv"
    return render_template('admin.html', lang=lang)

# @app.route('/en')
# def en():
#     lang = "en"
#     return render_template('index.html', lang=lang)

# @app.route('/no')
# def no():
    # lang = "nb"
    # return render_template('index.html', lang=lang)

# @app.route('/admin')
# def admin():
#     return render_template('admin.html')
