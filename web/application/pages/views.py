from application.pages import app
from flask import request, redirect, url_for,render_template
@app.route('/')
def show_home():
    return render_template('entries/index.html')