import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# установка инструментария
# pip3 install flask sqlalchemy flask-sqlalchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)


db.drop_all()  # перед созданием таблицы удаляем данные старой таблицы (необязательно)
db.create_all()

user_jonn = User(name="Jonn", age=30)
user_kate = User(name="Kate", age=36)
user_yana = User(name="Yana", age=22)
user_lili = User(name="Lili", age=35)
user_platon = User(name="Platon", age=7)
# print(user_jonn, user_kate, user_yana, user_lili)

# db.session.add(user_jonn)
# db.session.add(user_kate)
users = [user_yana, user_kate, user_platon, user_jonn, user_lili, ]
db.session.add_all(users)

# print(db.session.new) # список недобавленных моделей

db.session.commit()  # подтверждаем внесение изменений в базу данных


@app.route("/users/first")
def get_first_user():
    user = User.query.first()
    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age,
    })


@app.route("/users/count")
def get_users_count():
    users_count = User.query.count()
    return json.dumps(users_count)


@app.route("/users")
def get_users():
    user_list = User.query.all()
    user_response = []
    for user in user_list:
        user_response.append({
            "id": user.id,
            "name": user.name,
            "age": user.age,
        })
    return json.dumps(user_response)


@app.route("/users/<int:sid>")
def get_user_by_id(sid):
    user = User.query.get(sid)

    if user is None:
        return "user not found"
    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age,
    })


if __name__ == '__main__':
    app.run(debug=True)
