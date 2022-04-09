from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
db = SQLAlchemy()

sub = '\n'+'_'*15

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    age = fields.Int()

print(f"{sub} серелизуем данные: ")
user = User(id=1, name="Anna", age=18)
user_schema = UserSchema()
result = user_schema.dump(user)
print(type(result), result["name"], result["age"])


print(f"{sub} готовим JSON структуру (переводим все в строку): ")
user = User(id=1, name="Anna", age=18)
user_schema = UserSchema()
result = user_schema.dumps(user)
print(type(result), result)


print(f"{sub} делаем дамп списка: ")
u1 = User(id=1, name="Anna", age=18)
u2 = User(id=2, name="Kety", age=21)
u3 = User(id=3, name="Yulia", age=28)
u4 = User(id=4, name="Mila", age=21)
u5 = User(id=5, name="Sonia", age=33)

user_schema = UserSchema(many=True)

print(type(user_schema.dump([u1, u2, u3, u4, u5])), user_schema.dump([u1, u2, u3, u4, u5]))
print(type(user_schema.dumps([u1, u2, u3, u4, u5])), user_schema.dumps([u1, u2, u3, u4, u5]))


print(f"{sub} десерелизация: ")
user_json_str = '{"age": 18, "name": "Anna"}'
user_schema = UserSchema()
user_dict = user_schema.loads(user_json_str)
user = User(**user_dict)
print(user.name, user.age)



if __name__ == '__main__':
    app.run(debug=True)