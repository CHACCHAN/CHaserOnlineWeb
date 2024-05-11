from flask import Blueprint, jsonify

apis_blueprint = Blueprint('apis', __name__)

@apis_blueprint.route('/fuck', methods=["GET"])
def get():
    print("メッセージを受け取りました")
    data = {"test":"Good"}
    return jsonify(data)