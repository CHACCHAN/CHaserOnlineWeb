import json
import os
from flask import Blueprint, request, jsonify, send_from_directory
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jti, get_jwt
)
from module import db, db_get, auth_jti
import bcrypt
import time
from logzero import logger
import traceback
from CHaserOnlineClient import CHaserOnlineController

setting_currentDir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(setting_currentDir, '../CHaserOnline/setting.json')
apis_blueprint = Blueprint('apis', __name__)

@apis_blueprint.route('/fuck', methods=['POST'])
def post():
    result = request.get_json()
    print(f'{result.get('url')}')
    data = {'test':'Good'}
    return jsonify(data)

#############################################################
# CHaserOnline API
@apis_blueprint.route('/chaseronline/js/<path:filename>')
def serve_chaser_files(filename)->any:
    return send_from_directory('../CHaserOnline', filename)

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

@apis_blueprint.route('/chaseronline/post/setting', methods=['POST'])
@jwt_required()
def post_setting()->dict:
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
            settings['CHaserOnlineServerURL'] = request.json.get('CHaserOnlineServerURL')
            settings['CHaserOnlineProxy'] = request.json.get('CHaserOnlineProxy')
    except FileNotFoundError:
        return jsonify({'status':'bad', 'message':f'Error: The file {json_path} does not exist.'}), 500
    except json.JSONDecodeError as e:
        return jsonify({'status':'bad', 'message':f'Error decoding JSON: {e}'}), 500
    
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
        return jsonify({'status':'ok', 'message': f'Updated settings: {settings}'}), 200
    except IOError as e:
        return jsonify({'status':'bad', 'message': f'Error writing JSON: {e}'}), 500
    
@apis_blueprint.route('/chaseronline/get/setting', methods=['GET'])
@jwt_required()
def get_setting()->dict:
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
            return jsonify({'status':'ok', 'data':settings}), 200
    except FileNotFoundError:
        return jsonify({'status':'bad', 'message':f'Error: The file {json_path} does not exist.'}), 500
    except json.JSONDecodeError as e:
        return jsonify({'status':'bad', 'message':f'Error decoding JSON: {e}'}), 500
    
#############################################################
# Auth API
@apis_blueprint.route('/get_user', methods=['GET'])
def get_user():
    sql = 'SELECT * FROM authinfo'
    try:
        users = db_get(sql)
        if not users:
            return jsonify({'mode': 'get', 'status': 'success', 'message': 'DB is empty'})
        
    except Exception as e:
        logger.error(traceback.format_exc())
        return jsonify({'message': 'An error occurred'}), 500
    
    return jsonify(users), 200  

@apis_blueprint.route('/signin', methods=['POST'])
def signin():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({'message': 'Format does not match'}), 400

    sql = 'SELECT user_id, username, password FROM authinfo WHERE username=?;'
    try:
        user = db(sql, [username])
        logger.debug(f'username={username}')
        if not user:
            return jsonify({'message': 'Bad username or password'}), 401

        logger.debug(f'{user}')
        if user['password'] == password:
            sql = 'UPDATE authinfo SET updated_at=? WHERE username=?;'
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            db(sql, [timestamp, username])
        else:
            return jsonify({'message': 'Bad username or password'}), 401
    except Exception as e:
        logger.error(traceback.format_exc())
        return jsonify({'message': 'An error occurred'}), 500

    access_token = create_access_token(identity=user['user_id'])
    sql = 'UPDATE authinfo SET jti=? WHERE username=?;'
    db(sql, [get_jti(access_token), username])

    return jsonify(access_token=access_token), 200

@apis_blueprint.route('/require', methods=['GET', 'POST'])
def require():
    if not request.is_json:
        return jsonify({'message': 'Missing JSON in request'}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    print(f'require request: username={username}, password={password}')

    sql = 'SELECT * FROM authinfo WHERE username=?;'
    if db(sql, [username]):
        return jsonify({'mode': 'require', 'status': 'error', 'message': 'This username cannot be used'}), 400
    
    sql = 'INSERT INTO authinfo (username, password) VALUES (?, ?);'
    db(sql, [username, password])
    return jsonify({'mode': 'require', 'status': 'success', 'message': 'Completed'}), 200

@apis_blueprint.route('/remove', methods=['POST'])
@jwt_required()
def remove():
    user_id = request.json.get('user_id', None)
    if not user_id:
        return jsonify({'message': 'Format does not match'}), 400
    
    sql = 'DELETE FROM authinfo WHERE user_id=?'
    db(sql, [user_id])
    
    return jsonify({'status': 'ok'})
    
@apis_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    user = auth_jti(get_jwt_identity(), get_jwt()['jti'])
    if not user:
        return jsonify({'message': 'Bad access token'}), 401
    
    sql = 'SELECT * FROM authinfo WHERE username=?;'
    currentUser =  db(sql, [user.get('username')])

    return jsonify({'status': 'ok', 'username': currentUser.get('username'), 'password': currentUser.get('password')}), 200
