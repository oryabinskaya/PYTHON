
while True:
    time = input('Введите время в секундах\n')
    if time.isdigit():
        time = f'{int(time)//3600:>02}:{int(time)//60%60:>02}:{int(time)%60:>02}'
        print (time)
        break
    else:
        print ('Ошибка ввода,введите число')

