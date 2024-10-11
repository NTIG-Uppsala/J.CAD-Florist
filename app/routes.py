from flask import render_template
from app import app

@app.route('/')
@app.route('/se')
def se():
    lang = "sv"
    return render_template('index.html', lang=lang)

@app.route('/admin')
def admin():
    lang = "sv"
    return render_template('admin.html', lang=lang)