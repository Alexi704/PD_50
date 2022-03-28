import sqlite3
from os.path import join, isfile

from config import DATABASE_PATH, SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH, DATA_MIGRATION_FILE_PATH


def get_sql_from_file(file_name):
    """
    Получает чистый SQL из файла.
    :param file_name: Полный путь до файла.
    :return: Строка с SQL запросом.
    """
    content = ''
    if isfile(file_name):
        with open(file_name) as file:
            content = file.read()
    return content


def main():
    """
    Основная функция. Выполняет миграцию данных.
    """
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Создаем структуру базы данных
    init_sql = get_sql_from_file(join(SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH))
    cursor.executescript(init_sql)

    # Заполняем данными
    data_sql = get_sql_from_file(join(SQL_DIR_PATH, DATA_MIGRATION_FILE_PATH))
    cursor.executescript(data_sql)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
