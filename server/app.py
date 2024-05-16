import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
server_dir = os.path.join(parent_dir, "server")
sys.path.append(server_dir)

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes import routes_blueprint
from apis import apis_blueprint

app = Flask(__name__, static_folder='../web/dist/static', template_folder='../web/dist')
jwt = JWTManager(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SECRET_KEY'] = os.urandom(24)
app.register_blueprint(apis_blueprint, url_prefix='/api')
app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    