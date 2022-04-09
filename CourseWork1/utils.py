import requests
import random


class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def check_word_in_subwords(self, user_input):
        """проверка введенного слова в списке допустимых подслов (bool)"""
        if user_input in self.subwords:
            return True

    def count_subwords(self):
        """подсчет количества подслов (int)"""
        return len(self.subwords)


class Player:
    def __init__(self, user_name):
        self.user_name = user_name
        self.user_words_used = []

    def count_words(self, words):
        """получаем количество исходных слов (int)"""
        return len(words)

    def add_to_used(self, user_input):
        """добавляем слова в список использованных слов (ничего не возвращает)"""
        self.user_words_used.append(user_input)

    def is_word_used(self, user_input):
        """проверяем, было ли слово использовано (bool)"""
        if user_input in self.user_words_used:
            return True


def load_random_word():
    """ - получаем список слов с внешнего ресурса """
    data_word = requests.get('https://jsonkeeper.com/b/KOYZ').json()  # получаем свои данные
    # data_word = requests.get('https://jsonkeeper.com/b/C6L5').json()  # получаем данные что прописаны в задаче

    """ - выбираем случайное слово """
    random.shuffle(data_word)  # перемешиваем список
    word = data_word[0]['word']
    subwords = data_word[0]['subwords']  # поулчаем случайное слово из перемешенного списка для дальнейшей игры
    # print(word, subwords)

    """ - создаем экземпляр класса BasicWord """
    basic_word = BasicWord(word, subwords)

    """ - возвращаем этот экземпляр """
    return basic_word


def main():
    user_name = input('Ввведите имя игрока: ')

    print(f'Привет, {user_name}!')

    data = load_random_word()
    count_subwords = len(data.subwords)
    player = Player(user_name)

    print(f'Можно составить {count_subwords} слов из слова {data.word.upper()} (попыток: {count_subwords}).')
    print('Слова должны быть не короче 3 букв.\n'
          '(вы всегда можете остановить игру, набрав на клавиатуре "стоп" или "stop"\n'
          'Поехали, ваше первое слово?')

    for subword in range(count_subwords):
        user_input = input('Введите слово: ')
        while len(user_input) < 3:
            user_input = input('слово не должно быть короче 3-х символов: ')

        """у введенного значения обрезаем лишние пробелы, переводим в нижний регистр 
        и в случае ввода больше 1-го слова берем тольео первое слово"""
        user_input = user_input.strip().lower().split()[0]
        if user_input in ['стоп', 'stop']:  # завершаем игру
            break

        used_word = data.check_word_in_subwords(user_input)
        if user_input in player.user_words_used:
            print('вы уже угадывали это слово')
        elif used_word:
            player.add_to_used(user_input)
            print(f'Верно!')
        else:
            print('Такого слова нет.')

    print(f'Игра завершена, вы угадали {len(player.user_words_used)} из {count_subwords} возможных.')