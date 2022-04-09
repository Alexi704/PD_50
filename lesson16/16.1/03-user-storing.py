from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# установка инструментария
# pip3 install flask sqlalchemy flask-sqlalchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

# db.drop_all()
db.create_all()

user_jonn = User(name="Jonn", age=30)
user_kate = User(name="Kate", age=32)
print(user_jonn, user_kate)

# db.session.add(user_jonn)
# db.session.add(user_kate)

users = [user_kate, user_jonn]
db.session.add_all(users)

print(db.session.new) # список недобавленных моделей

db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
