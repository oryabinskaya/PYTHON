while True:
    number = input('Введите число\n')
    if number.isdigit():
        print (sum(map(int,(number,number*2,number*3))))
        break
    else:
        print ('Ошибка ввода,введите число')

