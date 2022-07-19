#  9. Среди натуральных чисел, которые были введены, 
#  найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

print('Вводите числа одно за другим, для выхода введите 0') 
max_sum = 0 
max_sum_num = '' 
while True: 
    user_num = input('Введите число: ') 
 
    new_max_sum = 0 
    for n in user_num: 
        new_max_sum += int(n) 
 
    if max_sum < new_max_sum: 
        max_sum =  new_max_sum 
        max_sum_num = user_num 
     
    if user_num == '0': 
        break 
 
print(f'{max_sum_num} - {max_sum}')
