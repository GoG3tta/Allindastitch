from flask import Flask

DATABASE = 'pythonProject' # CHANGE PROJECT_SCHEMA TO SQL SCHEMA

app = Flask(__name__)
app.secret_key = 'this is my key'