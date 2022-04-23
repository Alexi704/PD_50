from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def page_index():
    page_content = """
    <h2><a href="/hello">Hello</a></h2>
    <h2><a href="/cycle">Cycle</a></h2>
    <h2><a href="/blocked">Blocked</a></h2>
    """
    return page_content


@app.route('/hello')
def page_hello():
    user_data = {
        'name': 'Ivan',
        'phone': '+7 123 456 78 90',
        'email': 'ivan_dev@gmail.com',
        'telegram': 'ivan_dev',
    }
    return render_template('hello.html', user=user_data)


@app.route('/cycle')
def page_cycle():
    items = ["Python", "Java", "Kotlin", "Go"]
    return render_template('cycle.html', items=items)


@app.route('/blocked')
def page_blocked():
    is_blocked = True  # Или is_blocked = False
    return render_template('blocked.html', is_blocked=is_blocked)


if __name__ == '__main__':
    app.run()
