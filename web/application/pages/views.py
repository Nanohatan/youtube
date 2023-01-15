from application.pages import app
@app.route('/')
def show_home():
    return "home is here"