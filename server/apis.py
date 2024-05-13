from flask import Blueprint, request, jsonify
from CHaserOnlineClient import CHaserOnlineController

apis_blueprint = Blueprint('apis', __name__)

@apis_blueprint.route('/fuck', methods=["POST"])
def post():
    result = request.get_json()
    print(f'{result.get('url')}')
    data = {"test":"Good"}
    return jsonify(data)

# @param
# return -> 接続結果を返します[object]
# {'status':'ok'} -> 接続完了
# {'status':'bad'} -> 接続失敗
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
        return jsonify({'status':'ok'})
    else:
        return jsonify({'status':'bad'})

# @param
# return -> 3x3マス分の9つのブロック情報が返ります[dict]
# ["0", "11", "12", "13", "0", "11", "12", "13", "0"](例)
@apis_blueprint.route('/chaseronline/getready', methods=['POST'])
def getready()->dict:
    requests = request.get_json()
    _CHaserOnlineClient.getready(GetReadyMode=requests.get('GetReadyMode'))
    result = _CHaserOnlineClient.returnNumber()
    
    return jsonify(result)

# @param
# return -> 3x3マス分の9つのブロック情報が返ります[dict]
# ["0", "11", "12", "13", "0", "11", "12", "13", "0"](例)
@apis_blueprint.route('/chaseronline/action', methods=['POST'])
def action()->dict:
    requests = request.get_json()
    _CHaserOnlineClient.action(mode=requests.get('mode'))
    result = _CHaserOnlineClient.returnNumber()
    _CHaserOnlineClient.complete()
    
    return jsonify(result)

# @param
# return -> ゲーム終了の真偽値が返ります[bool]
# True -> 終了(または異常終了) False -> 実行中
@apis_blueprint.route('/chaseronline/gameset', methods=['GET'])
def gameSet()->bool:
    return jsonify(_CHaserOnlineClient.gameSet())

# @param
# return -> ゲームのターン数が返ります[int]
@apis_blueprint.route('/chaseronline/gameturn', methods=['GET'])
def gameTurn()->int:
    return jsonify(_CHaserOnlineClient.gameTurn())