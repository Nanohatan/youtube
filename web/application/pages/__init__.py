from flask import Flask
app = Flask(__name__)
app.config.from_object('application.pages.config')

import application.pages.views