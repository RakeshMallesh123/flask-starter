from flask import Flask, redirect, url_for, jsonify, request, Markup
# from flask_login import current_user, login_required
from flask_admin import Admin, AdminIndexView
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla.view import ModelView
from config import PAGE_SIZE


class BaseModelView(ModelView):
    page_size = PAGE_SIZE

    # def is_accessible(self):
    #     return current_user.is_authenticated

    # def inaccessible_callback(self, name, **kwargs):
    #     return redirect(url_for('auth.login'))


class UserModelView(BaseModelView):
    column_list = ('id', 'username', 'email', 'address', 'is_active')
    column_labels = dict(username='User Name', )
    can_view_details = True
    can_create = False
    column_default_sort = ('id', True)


class MyAdminIndexView(AdminIndexView):
    # def is_accessible(self):
    #     return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))


class LogoutMenuLink(MenuLink):
    # def is_accessible(self):
    #     return current_user.is_authenticated
    pass
