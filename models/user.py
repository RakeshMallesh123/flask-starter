from db import db
import datetime
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash


class BaseModel:
    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    # Soft delete
    def delete_from_db(self) -> None:
        self.deleted_at = datetime.datetime.now()
        db.session.add(self)
        db.session.commit()


class UserModel(db.Model, BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    is_active = db.Column(db.Boolean, default=True)
    is_email_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email, deleted_at=None).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def encrypt_password(cls, password):
        return generate_password_hash(password, method='sha256')
