# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

action = input('''Введите тип диопазона который вы хотитие получить.\n
int == 1\n
float == 2\n
symbol == 3 \t:''')
 
a = input('Введите перевое число или символ ')
b = input('Введите второе число или символ ')

if action == '1':
    if int(a) < int(b):
        print(random.randint(int(a), int(b)))
    else:
        print(random.randint(int(b), int(a)))
elif action == '2':
    if float(a) < float(b):
        print(random.uniform(float(a), float(b)))
    else:
        print(random.uniform(float(b), float(a)))
else:
    if ord(a) < ord(b):
        print(chr(random.randint(ord(a), ord(b))))
    else:
        print(chr(random.randint(ord(b), ord(a))))
