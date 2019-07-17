from db import db

from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash

from models.base_model import BaseModel


class AccountModel(UserMixin, db.Model, BaseModel):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200))
    role = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))

    @classmethod
    def encrypt_password(cls, password):
        return generate_password_hash(password, method='sha256')
