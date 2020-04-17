while True:
    number = input('Введите число\n')
    if number.isdigit():
        number = int(number)
        result = number % 10
        number = number // 10
        while number > 0:
            if number % 10 > result:
                result = number % 10
            number = number // 10
        print(result)
        break
    else:
        print ('Ошибка ввода,введите число')

