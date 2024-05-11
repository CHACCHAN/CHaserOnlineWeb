from flask import Blueprint, render_template

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/', defaults={'path': ''})
@routes_blueprint.route('/<path:path>')
def index(path):
    return render_template('index.html')