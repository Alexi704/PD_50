import sqlite3
from pprint import pprint as pp

PATH_BD = 'netflix.db'


def film_by_name(film_name):
    """ Ищем фильм по вхождению названия фильма """
    with sqlite3.connect(PATH_BD) as connection:
        cursor = connection.cursor()
        query = """
                SELECT title, country, release_year, listed_in, description 
                FROM netflix WHERE title != ''
                """
        result = cursor.execute(query)

    film_name = film_name.lower()
    films_found = []
    for item in result:
        film_name_in_bd = item[0].lower()
        if film_name in film_name_in_bd:
            film_found = {
                "title": item[0],
                "country": item[1],
                "release_year": item[2],
                "genre": item[3],
                "description": item[4]
            }
            films_found.append(film_found)
    return films_found


def film_year_to_year(first_year, last_year):
    """ Ищем фильмы по диапазону годов """
    with sqlite3.connect(PATH_BD) as connection:
        cursor = connection.cursor()
        query = """
            SELECT title, release_year
            FROM netflix
            WHERE title != '' AND release_year BETWEEN ? AND ?
        """
        result = cursor.execute(query, (first_year, last_year))
    film_year_to_year_list = []
    for item in result:
        film_found = {
            "title": item[0],
            "release_year": item[1]
        }
        film_year_to_year_list.append(film_found)
    return film_year_to_year_list


def film_by_rating(age_limit):
    """ Ищем фильмы в зависимости от возврастного рейтинга"""
    with sqlite3.connect(PATH_BD) as connection:
        cursor = connection.cursor()
        if age_limit == 'children':
            query = """
                SELECT title, rating, description
                FROM netflix
                WHERE title != '' AND rating != ''
                AND rating IN ('G')
            """
        elif age_limit == 'family':
            query = """
               SELECT title, rating, description
               FROM netflix
               WHERE title != '' AND rating != ''
               AND rating IN ('G', 'PG', 'PG-13')
           """
        elif age_limit == 'adult':
            query = """
                  SELECT title, rating, description
                  FROM netflix
                  WHERE title != '' AND rating != ''
                  AND rating IN ('R', 'NC-17')
              """
        else:
            query = """
                   SELECT title, rating, description
                   FROM netflix
                   WHERE title != '' AND rating != ''
               """
        result = cursor.execute(query)

    films_found_age_limit = []
    for item in result:
        film_found = {
            "title": item[0],
            "rating": item[1],
            "description": item[2]
        }
        films_found_age_limit.append(film_found)
    return films_found_age_limit
# pp(film_by_rating('children'))
# pp(film_by_rating('family'))
# pp(film_by_rating('adult'))


def film_genre(genre):
    """ Поиск фильмов по жанру """
    genre = (['%' + genre + '%'])
    with sqlite3.connect(PATH_BD) as connection:
        cursor = connection.cursor()
        query = """
            SELECT title, description, listed_in
            FROM netflix
            WHERE title != '' 
            AND listed_in LIKE ?
            ORDER BY release_year DESC
            LIMIT 10
        """
        result = cursor.execute(query, genre)
    films_found_genre = []
    for item in result:
        film_found = {
            "title": item[0],
            "description": item[1],
            "genre": item[2],
        }
        films_found_genre.append(film_found)
    return films_found_genre
# pp(film_genre('Dramas'))


def search_actors_who_played_together(actor_1, actor_2):
    """ Поиск двух актеров и тех, кто играет с ними в паре больше 2 раз """
    with sqlite3.connect(PATH_BD) as connection:
        cursor = connection.cursor()
        query = """
                SELECT "cast"
                FROM netflix
                WHERE "cast" LIKE ? OR ?
                """
        result = cursor.execute(query, ('%' + actor_1 + '%', '%' + actor_2 + '%',))

    """ Актеры, играющие вместе с нашими актерами """
    all_acters = []
    for item in result:
        the_cast_of_the_film = ' '.join(item).split(', ')
        for i in the_cast_of_the_film:
            all_acters.append(i)

    """ Убираем из списка актеров первоначального поиска"""
    while actor_1 in all_acters:
        all_acters.remove(actor_1)
    while actor_2 in all_acters:
        all_acters.remove(actor_2)

    """ делаем выборку актеров, игравших более 2-х раз """
    uniq_list_acters = set(all_acters)  # получаем уникальный список актеров

    acters_played_more_times = {}
    for acter in uniq_list_acters:
        """ добавляем в словарь актеров, сыгравших более ... раз
            реализовано через словарь, чтобы наглядно видеть, кто и сколько раз учавствовал
            можно сразу выводить через список, так проще, но... данный метод более нагляден """
        if all_acters.count(acter) > 2:
            acters_played_more_times[acter] = all_acters.count(acter)
    """ Получаем актеров списком """
    list_acters_played_more_times = list(acters_played_more_times.keys())
    return list_acters_played_more_times
""" проверяем ..."""
print('Эти актеры сыграли с нашими атерами более чем 2 раза:')
print(search_actors_who_played_together('Rose McIver', 'Ben Lamb'))
print(search_actors_who_played_together('Jack Black', 'Dustin Hoffman'))
print('-'*40)


def search_films_by_type_release_year(input_type, input_release_year, input_listed_in):
    """ получаем список картин, передав в функцию ее тип (фильм или сериал), год выпуска и жанр """
    with sqlite3.connect(PATH_BD) as connection:
        cursor = connection.cursor()
        query = """
                SELECT title, description
                FROM netflix
                WHERE type = ?
                AND release_year = ?
                AND listed_in LIKE ?
                """
        result = cursor.execute(query, (input_type, input_release_year, '%' + input_listed_in + '%',))

    films_found_by_type_relise_year = []
    for item in result:
        film_found = {
            "title": item[0],
            "description": item[1],
        }
        films_found_by_type_relise_year.append(film_found)
    return films_found_by_type_relise_year


""" проверяем ..."""
print('Поиск фильмов по: типу, году выпуска и жанру:')
pp(search_films_by_type_release_year('Movie', 2020, 'Action'))
print('-'*40)
