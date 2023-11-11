from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from uuid import uuid1

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid1())

# 设置 JWT 存储的位置为 cookies
# app.config['JWT_TOKEN_LOCATION'] = ['cookies']

jwt = JWTManager(app)
jwt.init_app(app)

CORS(app, supports_credentials = True)

from routes.api import apiBp
app.register_blueprint(apiBp)

if __name__ == '__main__':
    app.run(debug = False, host = '127.0.0.1', port = 8001)