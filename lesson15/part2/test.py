user_input = input('Введите цифры 1 и 0: ')

str_output = ''

for i in user_input:
    if i == '1':
        str_output += 'True'
    elif i == '0':
        str_output += 'False'
    else:
        str_output += ''

print(str_output)
