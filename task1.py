# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

day=int(input("Введите день недели п/п:  "))
if day<1 or day>7:
    print('Неверное число')
if 0<day<6:
    print ('Нет, будний день')
if day==6 or day==7:
    print('Да, выходной день')










