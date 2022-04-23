import datetime, decimal, json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

#### Шаг 1 ####
print('-'*20 + 'Шаг 1' + '-'*20)

a = "Hello World!"
b = {"filed": "value"}
c = [1,5,15]
print(json.dumps(a))
print(json.dumps(b))
print(json.dumps(c))

#### Шаг 2 ####
# print('-'*20 + 'Шаг 2' + '-'*20)

a = datetime.datetime.now()
b = decimal.Decimal(3)
# print(json.dumps(a)) # упадет с ошибкой, т.к. json не умеет сериализовывать нестроковые значения
# print(json.dumps(b)) # упадет с ошибкой, т.к. json не умеет сериализовывать нестроковые значения

#### Шаг 3 ####
print('-'*20 + 'Шаг 3' + '-'*20)

# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     age = db.Column(db.Integer)
#
# u = User(name="Jonn", age=30)
# print(json.dumps(u)) # упадет с ошибкой, т.к. json не умеет сериализовывать объекты


#### Шаг 4 ####
# print('-'*20 + 'Шаг 4' + '-'*20)
a = "Hello World!"
b = '{"filed": "value"}'
c = "[1,5,15]"
# print(json.loads(a)) # упадет с ошибкой, т.к. json не может загружать строки без заданной структуры данных
print(json.loads(b)["filed"]) # отработает нормально, т.к. задана структура json
print(json.loads(c)[1]) # отработает нормально, т.к. задана структура json


if __name__ == '__main__':
    app.run(debug=True)
