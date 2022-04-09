import logging
from os import abort

from flask import Flask, jsonify, request, Blueprint
from utils import Posts

app = Flask(__name__)
logging.basicConfig(filename="basic.log", encoding='utf-8')
blueprint_api = Blueprint('blueprint_api', __name__, template_folder='templates', static_folder='static')
DATA_PATH = "data/data.json"


@blueprint_api.route('/api/posts', methods=['GET'])
def index_api_posts():
    post_data = Posts(DATA_PATH)
    return jsonify(post_data.get_posts_all())


@blueprint_api.route('/api/posts/<post_id>', methods=['GET'])
def one_api_post(post_id):
    post_data = Posts(DATA_PATH)
    post = post_data.get_post_by_pk(int(post_id))
    return jsonify(post)



