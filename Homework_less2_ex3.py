#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится  месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
season_dict = {1:'Зима', 2:'Весна',3:'Лето',4:'Осень'}
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
ulist = int(input("Напишите номер месяца\n"))
if ulist == 1 or ulist  == 2 or ulist  == 12 :
    print(season_list[0])
    print(season_dict.pop(1))
elif ulist  == 3 or ulist  == 4 or ulist  == 5 :
    print(season_list[1])
    print(season_dict.pop(2))
elif ulist  == 6 or ulist  == 7 or ulist  == 8 :
    print(season_list[2])
    print(season_dict.pop(3))
elif ulist  == 9 or ulist  == 10 or ulist  == 11 :
    print(season_list[3])
    print(season_dict.pop(4))
else:
    print("Вы ввели не сущестующий месяц, попробуйте снова")