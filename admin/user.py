from admin.views import BaseModelView


class UserModelView(BaseModelView):
    column_list = ('id', 'username', 'email', 'address', 'is_active', 'created_at')
    column_labels = dict(username='User Name', )
    form_excluded_columns = ('is_email_verified', 'password', 'created_at', 'updated_at', 'deleted_at')
    can_view_details = True
    can_create = False
    column_default_sort = ('id', True)