def get_period(hour):
    if type(hour) != int: raise TypeError("Должно быть int")
    if hour < 0 or hour > 24: raise ValueError("Допустимое значение 0-24")


    if hour < 7:
        return "ночь"
    elif hour < 12:
        return "утро"
    elif hour < 18:
        return "день"
    else:
        return "вечер"
