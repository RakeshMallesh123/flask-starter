from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from models.account import AccountModel
from libs.strings import gettext


auth = Blueprint('auth', __name__)


@auth.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = AccountModel.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash(gettext("user_invalid_credentials"))
        return redirect(url_for("auth.login"))  # if user doesn't exist or password is wrong, reload the page

    login_user(user, remember=remember)
    return redirect(url_for("admin.index"))


@auth.route("/signup")
def signup():
    return render_template("signup.html")


@auth.route('/signup', methods=["POST"])
def signup_post():
    email = request.form.get("email")
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    password = request.form.get("password")

    user = AccountModel.query.filter_by(email=email).first()

    if user:
        flash(gettext("user_email_exists"))
        return redirect(url_for("auth.signup"))

    new_user = AccountModel(email=email, firstname=firstname, lastname=lastname,
                            password=AccountModel.encrypt_password(password))
    new_user.save_to_db()

    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.index"))
