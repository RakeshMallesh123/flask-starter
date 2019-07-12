import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from marshmallow import ValidationError
from flask_sendgrid import SendGrid

from db import db
from ma import ma
from resources.v1.user import UserRegister, UserLogin, User, UserLogout, TokenRefresh


app = Flask(__name__)
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")
api = Api(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
mail = SendGrid(app)


# @app.before_first_request
# def create_tables():
#     db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


# API V1 Start
api_v1 = '/api/v1'
api.add_resource(UserRegister, api_v1+"/register")
api.add_resource(User, api_v1+"/user/<int:user_id>")
api.add_resource(UserLogin, api_v1+"/login")
api.add_resource(UserLogout, api_v1+"/logout")
api.add_resource(TokenRefresh, api_v1+"/refresh")
# API V1 End

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5001, debug=True)
