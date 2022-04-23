import utils
from flask import Flask

app = Flask(__name__)


@app.route('/')
def page_main():
    return utils.get_all_candidates()


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    return utils.get_candidate_for_uid(uid)


@app.route('/skill/<skill>')
def page_skills(skill):
    return utils.get_candidates_for_skill(skill)


if __name__ == "__main__":
    app.run()
