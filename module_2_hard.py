import random

# выбираем случайным образом число в первом поле
first_number = random.randrange(3, 20)
print(f'Число из первой вставки: {first_number}')
result = ''

for first in range(1, int(first_number / 2) + 1):
    second = first + 1
    while second < first_number and first + second <= first_number:
        second_number = first + second
        if first_number % second_number == 0:
            result += f'{first}{second}'
        second += 1
print(f'Пароль для остановки шипов: {result}')
