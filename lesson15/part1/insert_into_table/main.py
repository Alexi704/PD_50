# Добавление данных в таблицу
#
# Добавьте в БД следующих животных:
#
# +----+------------+-------+-----+-------------+-----+--------+
# | Id | AnimalType |  Name | Sex | DateOfBirth | Age | Weight |
# +----+------------+-------+-----+-------------+-----+--------+
# | 1  |   Кошка    |  Соня |  Ж  |  2013-12-02 |  7  |  2.15  |
# | 2  |    Кот     | Семен |  М  |  2017-05-03 |  4  |  4.5   |
# | 3  |   Собака   | Алина |  Ж  |  2018-11-12 |  2  |  20.8  |
# | 4  |    Пес     | Бобик |  М  |  2015-08-25 |  6  |  5.75  |
# +----+------------+-------+-----+-------------+-----+--------+
#
#
import sqlite3
import prettytable
# from tools import create_table

con = sqlite3.connect("memory2.db")
# con = create_table(con)  # сформируем таблицу из предыдущих уроков
cur = con.cursor()
# sqlite_query = ("""
#                 CREATE TABLE IF NOT EXISTS animal_1 (
#                 Id integer PRIMARY KEY AUTOINCREMENT,
#                 AnimalType varchar(50) NOT NULL,
#                 Sex varchar(50),
#                 Name varchar(50) NOT NULL DEFAULT 'Noname',
#                 DateOfBirth date,
#                 Age integer,
#                 Weight decimal)
#                 """)  # TODO составьте запрос на добавление данных в таблицу
sqlite_query = ("""
                INSERT INTO animal_1
                ("AnimalType", "Name", "Sex", "DateOfBirth", "Age", "Weight")
                VALUES
                ('Кошка', 'Соня', 'Ж', '2013-12-02', 7, 2.15),
                ('Кот', 'Семен', 'М', '2017-05-03', 4, 4.5),
                ('Собака', 'Алина', 'Ж', '2018-11-12', 2, 20.8),
                ('Пес', 'Бобик', 'М', '2015-08-25', 6, 5.75)
                """)  # TODO составьте запрос на добавление данных в таблицу

# Не удаляйте этот код, он используется
# для вывода результата
cur.execute(sqlite_query)


def print_result(sqlite_query):
    cur.execute(sqlite_query)
    result_query = ('SELECT * from animal_1')
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
