from flask_combo_jsonapi import ResourceList, ResourceDetail

from mainapp.blog.extensions import db
from mainapp.blog.models import Author
from mainapp.blog.schemas import AuthorSchema


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }