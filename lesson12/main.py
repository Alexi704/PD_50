from flask import Flask, request, render_template

# Импортируем блюпринты из их пакетов
from catalog.views import catalog_blueprint
from profile.views import profile_blueprint

app = Flask(__name__)

# Регистрируем первый блюпринт
app.register_blueprint(profile_blueprint)
# И второй тоже регистрируем
app.register_blueprint(catalog_blueprint)

app.run()
