from flask_combo_jsonapi import ResourceList, ResourceDetail

from mainapp.blog.api.permissions.user import UserListPermission, UserPatchPermission
from mainapp.blog.extensions import db
from mainapp.blog.models import User
from mainapp.blog.schemas import UserSchema


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_get': [UserListPermission],
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_patch': [UserPatchPermission],
    }