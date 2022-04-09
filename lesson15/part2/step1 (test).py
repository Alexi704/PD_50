import sqlite3

with sqlite3.connect('test.db') as connection:
    cursor = connection.cursor()
    query1 = f"""
                CREATE TABLE IF NOT EXISTS books (
                id integer PRIMARY KEY AUTOINCREMENT,
                book_name nvarchar(200) NOT NULL,
                description varchar,
                count_page integer,
                price_book decimal
                )
                """
    query2 = f"""
                INSERT INTO books
                ('book_name', 'description', 'count_page', "price_book")
                VALUES
                ('Курорты Баренцева моря', 'О самых знойных и популярных пляжах Баренцева моря', 500, 2500),
                ('Теория струн', 'О гавайской гитаре', 112, 620),
                ('Полет стрижа', 'Роман никому неизвестного писателя', 420, 700),
                ('Читаем вместе', 'Лучше один раз прочесть, чем 100 раз непрочесть!', 435, 999)
                """
    # cursor.execute(query1)
    # cursor.execute(query2)
