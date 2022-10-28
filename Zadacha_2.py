import random
from random import randint

candy = (2021)
print(f'У нас есть {candy} конфет')
handful = (28)
print(f'за один раз берем не более {handful} конфет')
print('Условие задачи: На столе лежит 2021 конфет. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более, чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
gamer_1 = input('Введите имя первого игрока : ')
gamer_2 = input('Введите имя второго игрока : ')
count = 0

x = randint(1, 2)
if x == 1:
    first = gamer_1
    second = gamer_2
else:
    first = gamer_2
    second = gamer_1

print(f'Поздравляю {first} ты ходишь первым !')
message = 'сколько конфет хотите взять?'

while candy > 0:
    if count == 0:

        print(f'{first}, {message}')
        num = int(input())
        if num > candy or num > handful:
            print(f' Можно взять не более {handful} конфет,попробуйте еще раз')
            num = int(input())
        candy = candy - num
    if candy > 0:
        print(f'Осталось {candy} конфет')
    else:
        print('Конфеты закончились :((')
    count = 1

    if count == 1:
        print(f'{second}, {message}')
        num = int(input())
        if num > candy or num > handful:
            print(f' Можно взять не более {handful} конфет,попробуйте еще раз')
            num = int(input())
        candy = candy - num
    if candy > 0:
        print(f'Осталось {candy} конфет')
    else:
        print('Конфеты закончились :((')
    count = 0

if count == 1:
    print(f'{second} ПОБЕДИЛ')
if count == 0:
    print(f'{first} ПОБЕДИЛ')
