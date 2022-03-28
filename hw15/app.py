from flask import Flask, jsonify
import sqlite3
from config import DATABASE_PATH, SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH, DATA_MIGRATION_FILE_PATH
from queries import GET_ANIMAL_BY_ID, GET_ANIMAL_BY_ID_SHORT_QUERY, GET_ANIMAL_BY_ID_FULL_QUERY


app = Flask(__name__)


def serilize_row(row: sqlite3.Row):
    return {key: row[key] for key in row.keys()}


@app.route('/<id>')
def get_animal_by_id(id):
    """представление по значению id из базы new_animals"""
    conn: sqlite3.Connection = app.config['db']
    cursor = conn.cursor()
    cursor.execute(GET_ANIMAL_BY_ID,(id, ))
    row = cursor.fetchone()
    cursor.close()
    return jsonify(serilize_row(row))


@app.route('/<animal_id>')
def get_animal_by_id_short(animal_id):
    """представление по уникальному значению (animal_id) из базы new_animals"""
    conn: sqlite3.Connection = app.config['db']
    cursor = conn.cursor()
    cursor.execute(GET_ANIMAL_BY_ID_SHORT_QUERY,(animal_id, ))
    row = cursor.fetchone()
    cursor.close()
    return jsonify(serilize_row(row))


@app.route('/<animal_id>/full')
def animal_id_full(animal_id):
    """полное представление по уникальному значению (animal_id) из базы new_animals"""
    conn: sqlite3.Connection = app.config['db']
    cursor = conn.cursor()
    cursor.execute(GET_ANIMAL_BY_ID_FULL_QUERY,(animal_id, ))
    row = cursor.fetchone()
    cursor.close()
    return jsonify(serilize_row(row))


if __name__ == '__main__':
    connection = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    app.config['db'] = connection
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        connection.close()
