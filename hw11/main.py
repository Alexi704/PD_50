from flask import Flask, render_template, url_for
import utils

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/list')
def page_list():
    user_qualities = utils.load_candidates_from_json()
    return render_template('list.html', user_qualities=user_qualities)


@app.route('/candidate/<int:uid>')
def page_single(uid):
    name, u_img, position, gender, age, skill = utils.get_candidate(uid)
    return render_template('single.html', name=name, u_img=u_img, position=position, gender=gender, age=age,
                           skill=skill)


@app.route('/search/')
def page_search_name():
    return render_template('search_begin.html')


@app.route('/search/<candidate_name>')
def page_search_candidate_name(candidate_name):
    search_candidate = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', search_candidate=search_candidate)


@app.route('/skill/')
def page_search_skill():
    return render_template('skill_begin.html')


@app.route('/skill/<skill_name>')
def page_search_skill_candidate(skill_name):
    search_candidate = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', search_candidate=search_candidate)


if __name__ == '__main__':
    app.run()
