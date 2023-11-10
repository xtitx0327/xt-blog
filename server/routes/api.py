from flask import Blueprint
from routes.apis.article import articleBp
from routes.apis.auth import authBp

apiBp = Blueprint('api', __name__, url_prefix = '/api')

apiBp.register_blueprint(authBp)
apiBp.register_blueprint(articleBp)