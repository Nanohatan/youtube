import json
import os
import random
import sys
import json

from flask import Flask, render_template, send_from_directory, url_for
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

@app.route('/')
def hello():
    return 'こんこん!'

@app.route('/wadai_deck')
def wadai_page():
    return render_template('wadai_deck.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)