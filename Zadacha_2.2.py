from random import *
import os


candy = 2021
handful = 28
gamer_1 = input('Как тебя зовут?: ')
gamer_2 = 'Компьютер'
gamers = [gamer_1, gamer_2]
print(f'Привет, {gamer_1}! твой соперник- компьютер!.')
message = 'Сколько конфет хотите взять?'
first = randint(-1, 0)
print(f'Поздравляю, {gamers[first+1]} ты ходишь первым !')

while candy > 0:
    first += 1

    if gamers[first % 2] == 'Компьютер':
        print(f'Ходит {gamers[first%2]} .Есть {candy} конфет. {message}: ')

        if candy < 29:
            num = candy
        else:
            div = candy//28
            num = candy - ((div*handful)+1)
            if num == -1:
                num = handful -1
            if num == 0:
                num = handful
        while num > 28 or num < 1:
            num = randint(1,28)
        print(num)
    else:
        num = int(input(f'Ходит,  {gamers[first%2]} Есть {candy} конфет. {message}:  '))
        while num > handful or num > candy:
            num = int(input(f'За один раз можно взять {handful} конфет, попробуй еще раз: '))
    candy = candy - num

print(f'У нас осталось {candy} конфетю .Победил {gamers[first%2]}')
