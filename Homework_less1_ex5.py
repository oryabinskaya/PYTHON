
revenue = float(input('Введите Выручку\n'))
cost = float(input('Введите Издержки\n'))
if revenue > cost:
    print ('В компании Прибыль')
    print ("%.0f%%" % (100 * ((revenue - cost)/revenue)))
    employees = int((input('Введите количество сотрудников в Компании\n')))
    print ('Прибыль фирмы в расчете на одного сотрудника составляет', round(((revenue - cost)/employees),2))
else:
    print('В компании Убыток')



