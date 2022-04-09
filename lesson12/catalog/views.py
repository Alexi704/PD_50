from flask import render_template, Blueprint

# Добавим настройку папки с шаблонами
catalog_blueprint = Blueprint('catalog_blueprint', __name__, template_folder='templates', url_prefix='/catalog')


# Добавим render_template
@catalog_blueprint.route('/')
def catalog_page():
    return render_template("main.html")


# Добавим render_template
@catalog_blueprint.route('/<cat>')
def category_page(cat):
    return render_template("category.html")


# Добавим render_template
@catalog_blueprint.route('/<cat>/<int:item>')
def item_page(cat, item):
    return render_template("item.html")
