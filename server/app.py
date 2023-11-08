from flask import Flask
from flask_jwt_extended import JWTManager
from uuid import uuid1

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid1())

jwt = JWTManager(app)
jwt.init_app(app)

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8006)