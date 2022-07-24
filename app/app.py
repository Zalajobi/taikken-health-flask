import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate

from app.admin import admin_blueprint
from app.auth import auth_blueprint, user_blueprint
from app.database import database
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# configure installed apps
app = Flask(__name__)
migrate = Migrate(app, database)
jwt = JWTManager(app)
CORS(app)
load_dotenv()
database.init_app(app)

# APP CONFIGS
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = os.getenv('SECRET_KEY')
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
app.config["SESSION_PERMANENT"] = False
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SESSION_TYPE"] = "filesystem"

#Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)


@app.route('/')
def hello_world():  # put application's code here
    return str(os.getenv('MAIL_USERNAME'))


@app.before_first_request
def create_tables():
    database.create_all()


if __name__ == '__main__':
    database.init_app(app)
    app.run(port=5000, debug=True)
