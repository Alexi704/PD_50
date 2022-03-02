# from main import ticket_price

assert ticket_price(0) == "Бесплатно", "Ошибка для 0 лет"
assert ticket_price(1) == "Бесплатно", "Ошибка для 1 лет"
assert ticket_price(7) == "100 рублей", "Ошибка для 7 лет"
assert ticket_price(18) == "200 рублей", "Ошибка для 18 лет"
assert ticket_price(25) == "300 рублей", "Ошибка для 25 лет"
assert ticket_price(60) == "Бесплатно", "Ошибка для 60 лет"
assert ticket_price(0.5) == "Бесплатно", "Ошибка для 0.5 лет"
assert ticket_price(-1) == "Ошибка", "Ошибка для -1 лет"

print("Все тесты пройдены!")  # Просто для веселья
