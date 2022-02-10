words = ['семь', 'семнадцать', 'пропуск', 'прочее', 'печенье', 'варенье', 'оригами', ]

user_input = input('введите что-нибудь для поиска: ').strip().lower()

for word in words:
    if user_input in word:
        print(word)
