#  1. Написать программу, которая будет складывать, вычитать,
#  умножать или делить два числа. Числа и знак операции вводятся пользователем.
#  После выполнения вычисления программа не завершается, 
#  а запрашивает новые данные для вычислений. 
#  Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
#  Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), 
#  программа должна сообщать об ошибке и снова запрашивать знак операции. 
#  Также она должна сообщать пользователю о невозможности деления на ноль, 
#  если он ввел его в качестве делителя.

while True:
    # Пользователь идеальный и вводит 3 элимента разделенные пробелом
    expression = input('Введите выражение типа \'a (+ - * /) b\': ').split()
    first_num = float(expression[0])
    second_num = float(expression[2])

    operator = expression[1]
    while operator not in '+-*/0':
        operator = input('Введите правельный оператор (+ - * /): ')
    
    if operator == '+':
        print(f'{first_num} {operator} {second_num} = {first_num + second_num}')

    elif operator == '-':
        print(f'{first_num} {operator} {second_num} = {first_num - second_num}')

    elif operator == '*':
        print(f'{first_num} {operator} {second_num} = {first_num * second_num}')
    
    elif operator == '/':
        if second_num != 0:
            print(f'{first_num} {operator} {second_num} = {first_num / second_num}')
        else:
            print('На 0 делить нельзя')
    else:
        break
    