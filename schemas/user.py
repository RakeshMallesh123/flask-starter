from ma import ma
from models.user import UserModel
from marshmallow import fields


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)

    email = fields.Email()


class LoginSchema(UserSchema):
    username = fields.Str(required=False)
