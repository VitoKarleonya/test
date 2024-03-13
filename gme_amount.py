
# Ввод пользователем загаданного числа
secret_number = int(input('Введите загаданное число: '))

while True:
    # Ввод пользователя для отгадывания числа
    guess = int(input('Отгадайте число: '))

    # Проверка условий
    if guess < secret_number:
        print('Мое число больше')
    elif guess > secret_number:
        print('Мое число меньше')     
    else:
    	print('Верно, это мое число!')
    	break