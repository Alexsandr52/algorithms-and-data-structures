# 4. Пользователь вводит две буквы. Определить, 
# на каких местах алфавита они стоят, и сколько между ними находится букв.

first_let = input('Введите первую букву ')
second_let = input('Введите вторую букву ')

print('Индекс букв в алфавите')
print(f'{first_let} = {ord(first_let) - 96}, {second_let} = {ord(second_let) - 96}')

if ord(first_let) < ord(second_let):
    print(f' между {first_let} и {second_let} {ord(second_let) - (ord(first_let)) } букв')
else:
    print(f'между {second_let} и {first_let} {ord(first_let) - (ord(second_let))} букв')
