from flask import Blueprint
from mainapp.blog.api.tag import TagList
from mainapp.blog.api.tag import TagDetail
from mainapp.blog.api.user import UserList
from mainapp.blog.api.user import UserDetail
from mainapp.blog.api.author import AuthorList
from mainapp.blog.api.author import AuthorDetail
from mainapp.blog.api.article import ArticleList
from mainapp.blog.api.article import ArticleDetail
from mainapp.blog.extensions import api, csrf

api_blueprint = Blueprint('api', __name__)
csrf.exempt(api_blueprint)

api.route(TagList, 'tag_list', '/api/tags/', tag='Tag', blueprint=api_blueprint)
api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag', blueprint=api_blueprint)

api.route(UserList, 'user_list', '/api/users/', tag='User', blueprint=api_blueprint)
api.route(UserDetail, 'user_detail', '/api/users/<int:id>', tag='User', blueprint=api_blueprint)

api.route(AuthorList, 'author_list', '/api/authors/', tag='Author', blueprint=api_blueprint)
api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>', tag='Author', blueprint=api_blueprint)

api.route(ArticleList, 'article_list', '/api/articles/', tag='Article', blueprint=api_blueprint)
api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>', tag='Article', blueprint=api_blueprint)