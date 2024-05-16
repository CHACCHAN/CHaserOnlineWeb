from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jti
)
from module import db, auth_jti
import bcrypt
import time
from logzero import logger
import traceback
from CHaserOnlineClient import CHaserOnlineController

apis_blueprint = Blueprint('apis', __name__)

@apis_blueprint.route('/fuck', methods=["POST"])
def post():
    result = request.get_json()
    print(f'{result.get('url')}')
    data = {"test":"Good"}
    return jsonify(data)

#############################################################
# CHaserOnline API
@apis_blueprint.route('/chaseronline/connect', methods=['POST'])
def connect()->object:
    global _CHaserOnlineClient
    requests = request.get_json()
    _CHaserOnlineClient = CHaserOnlineController(
        url=requests.get('url'),
        proxy=requests.get('proxy'),
        debug=requests.get('debug'),
        user=requests.get('user'),
        password=requests.get('password'),
        room=requests.get('room'),
    )
    result = _CHaserOnlineClient.connect()
    
    if result:
        return jsonify({'status':'ok'}), 200
    else:
        return jsonify({'status':'bad'}), 200

@apis_blueprint.route('/chaseronline/getready', methods=['POST'])
def getready()->dict:
    requests = request.get_json()
    _CHaserOnlineClient.getready(GetReadyMode=requests.get('GetReadyMode'))
    result = _CHaserOnlineClient.returnNumber()
    
    return jsonify(result), 200

@apis_blueprint.route('/chaseronline/action', methods=['POST'])
def action()->dict:
    requests = request.get_json()
    _CHaserOnlineClient.action(mode=requests.get('mode'))
    result = _CHaserOnlineClient.returnNumber()
    _CHaserOnlineClient.complete()
    
    return jsonify(result), 200

@apis_blueprint.route('/chaseronline/gameset', methods=['GET'])
def gameSet()->bool:
    return jsonify(_CHaserOnlineClient.gameSet()), 200

@apis_blueprint.route('/chaseronline/gameturn', methods=['GET'])
def gameTurn()->int:
    return jsonify(_CHaserOnlineClient.gameTurn()), 200

#############################################################
# Auth API
# @apis_blueprint.route("/signin", methods=["POST"])
# def signin():
#     username = request.json.get("username", None)
#     password = request.json.get("password", None)
#     if not username or not password:
#         return jsonify({"message": "Format does not match"}), 400

#     sql = "SELECT user_id, username, password FROM authinfo WHERE username=?;"
#     try:
#         user = db(sql, [username])
#         logger.debug(f'username={username}')
#         if not user:
#             return jsonify({"message": "Bad username or password"}), 401

#         logger.debug(f'{user}')
#         if bcrypt.checkpw(password.encode(), user["password"].encode()):
#             sql = "UPDATE authinfo SET updated_at=? WHERE username=?;"
#             timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#             db(sql, [timestamp, username])
#         else:
#             return jsonify({"message": "Bad username or password"}), 401
#     except Exception as e:
#         logger.error(traceback.format_exc())
#         return jsonify({"message": "An error occurred"}), 500

#     access_token = create_access_token(identity=user["user_id"])
#     sql = "UPDATE authinfo SET jti=? WHERE username=?;"
#     db(sql, [get_jti(access_token), username])

#     return jsonify(access_token=access_token), 200


# @apis_blueprint.route("/protected", methods=["GET"])
# @jwt_required
# def protected():
#     user = auth_jti(get_jwt_identity(), get_raw_jwt()["jti"])
#     if not user:
#         return jsonify({"message": "Bad access token"}), 401

#     return jsonify({"username": user["username"]}), 200


# @apis_blueprint.route("/signup", methods=["GET", "POST"])
# def signup():
#     if not request.is_json:
#         return jsonify({"message": "Missing JSON in request"}), 400
#     data = request.get_json()
#     username = data["username"]
#     password = data["password"]
#     password_conf = data["passwordConf"]

#     print(f'signup request: username={username}, password={password}, password_conf={password_conf}')

#     if username and username.encode().isalnum() and password != password_conf:
#         return jsonify({"mode": "signup", "status": "error", "message": "Format does not match"}), 400

#     sql = "SELECT * FROM authinfo WHERE username=?;"
#     if db(sql, [ username ]):
#         return jsonify({"mode": "signup", "status": "error", "message": "This username cannot be used"}), 400

#     salt = bcrypt.gensalt(rounds=10, prefix=b"2a")
#     hashed_pass = bcrypt.hashpw(password.encode(), salt).decode()
#     sql = "INSERT INTO authinfo (username, password) VALUES (?, ?);"
#     db(sql, [username, hashed_pass])
#     return jsonify({"mode": "signup", "status": "success", "message": "Completed"}), 200