import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from app.database import database
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Import models

# configure installed apps
app = Flask(__name__)
migrate = Migrate(app, database)
jwt = JWTManager(app)
CORS(app)
load_dotenv()

# APP CONFIGS
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = os.getenv('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route('/')
def hello_world():  # put application's code here
    return str(os.getenv('MAIL_USERNAME'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
