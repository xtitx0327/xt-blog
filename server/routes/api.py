from flask import Blueprint
from apis.article import articleBp
from apis.auth import authBp

apiBp = Blueprint('api', __name__, url_prefix = '/api')

apiBp.register_blueprint(articleBp)
apiBp.register_blueprint(authBp)