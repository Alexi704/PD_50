from flask import Flask, render_template, Blueprint, request
from utils import Posts
from pprint import pprint as pp

app = Flask(__name__)
blueprint_web = Blueprint('blueprint_web', __name__, template_folder='templates', static_folder='static')
DATA_PATH = "data/data.json"
COMMENT_PATH = "data/comments.json"


@blueprint_web.route('/', methods=['GET'])
def index():
    post_data = Posts(DATA_PATH)
    return render_template('index.html', posts=post_data.get_posts_all())


@blueprint_web.route('/post/<int:post_id>', methods=['GET'])
def get_post_by_post_id(post_id):
    post_data = Posts(DATA_PATH)
    content = post_data.get_post_by_pk(post_id)
    post_comment = Posts(COMMENT_PATH)
    comments = post_comment.get_comments_by_post_id(post_id)
    count_comment = len(comments)
    return render_template('post.html', content=content, post_id_=post_id,
                           comments=comments, count_comment=count_comment)


@blueprint_web.route('/search')
def search_for_posts():
    s = request.args.get('s', '')
    post_data = Posts(DATA_PATH)
    contents = post_data.search_for_posts(s)
    count_search_post = len(contents)
    return render_template('search.html', contents=contents, s=s, count_search_post=count_search_post)


@blueprint_web.route('/users/<username>')
def search_for_users_posts(username):
    post_data = Posts(DATA_PATH)
    posts = post_data.get_posts_by_user(username)
    return render_template('user-feed.html', username=username, posts=posts)
