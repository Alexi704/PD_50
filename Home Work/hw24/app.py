import os
import re
from typing import Iterator

from flask import Flask, request, Response
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def slice_limit(it: Iterator, value: int) -> Iterator:
    """
    change list to Iterator
    :param it: Iterator
    :param value: int
    :return: Iterator
    """
    i = 0
    for item in it:
        if i < value:
            yield item
        else:
            break
        i += 1


def build_query(it: Iterator, cmd: str, value: str) -> Iterator:
    res = map(lambda v: v.strip(), it)
    match cmd:
        case 'filter':
            return filter(lambda v: value in v, res)
        case 'sort':
            return iter(sorted(res, reverse=bool(value)))
        case 'unique':
            return iter(set(res))
        case 'limit':
            return slice_limit(res, int(value))
        case 'map':
            return map(lambda v: v.split(' ')[value], res)
        case 'regex':
            regex = re.compile(value)
            return filter(lambda x: regex.search(x), res)
    return res


@app.route("/perform_query")
def perform_query() -> Response:
    try:
        cmd_1 = request.args['cmd_1']
        cmd_2 = request.args['cmd_2']
        val_1 = request.args['val_1']
        val_2 = request.args['val_2']
        file_name = request.args['file_name']
    except:
        raise BadRequest(description='...incorrectly set arguments...')

    path_file = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(path_file):
        raise BadRequest(description=f'{file_name} was not found')

    with open(path_file, encoding='utf-8') as file:
        res = build_query(file, cmd_1, val_1)
        res = build_query(res, cmd_2, val_2)
        content = '\n'.join(res)

    return app.response_class(content, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
