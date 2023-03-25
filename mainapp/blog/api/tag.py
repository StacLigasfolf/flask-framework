from flask_combo_jsonapi import ResourceList, ResourceDetail

from mainapp.blog.extensions import db
from mainapp.blog.models import Tag
from mainapp.blog.schemas import TagSchema


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }