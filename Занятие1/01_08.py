# 8. Вводятся три разных числа. 
# Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

if a > b and a < c or a > c and a < b:
    print(f'Среднее число {a}')

elif b > a and b < c or b > c and b < a:
    print(f'Среднее число {b}')

else:
    print(f'Среднее число {c}')
    