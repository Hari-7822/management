from app import app

@app.route("/")
def hi():
    return 'Home'

@app.route("/new")
def new():
    return "New"

@app.route("/One")
def One():
    return "Success"
    