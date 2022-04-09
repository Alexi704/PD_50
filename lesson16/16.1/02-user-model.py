from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

# установка инструментария
# pip3 install flask sqlalchemy flask-sqlalchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    age = Column(Integer)

db.create_all()

user_jonn = User(name="Jonn", age=30)
user_kate = User(name="Kate", age=32)

print(user_jonn, user_kate)

if __name__ == '__main__':
    app.run(debug=True)