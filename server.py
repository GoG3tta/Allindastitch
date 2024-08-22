from flask_app import app
from flask_app.models import project # CHANGE PROJECT TO FILE NAME IN YOUR MODELS FOLDER


if __name__ == '__main__':
    app.run(debug=True)