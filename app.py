from flask import Flask

app = Flask(__name__, template_folder="template")

from config import *
from routes import *

if __name__ == "__main__":
    app.run(debug=True)