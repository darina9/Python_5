def image_field(field):
    print("-------------")
    for i in range(3):
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-------------")

def entering_values(icon):
    valid = False
    while not valid:
        answer = input("Выберите номер на игровом поле для  " + icon+"? ")
        try:
            answer = int(answer)
        except:
            print("Ошибка")
            continue
        if answer >= 1 and answer <= 9:
            if (str(field[answer-1]) not in "XO"):
                field[answer-1] = icon
                valid = True
            else:
                print("Эта позиция уже заполнена")
        else:
            print("Ошибка. Введенное значение не входит в диапазон от 1 до 9.")


def who_win(field):
    win_position = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_position:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False

def main(field):
    count = 0
    win = False
    while not win:
        image_field(field)
        if count % 2 == 0:
            entering_values("X")
        else:
            entering_values("O")
        count += 1
        if count > 4:
            temp = who_win(field)
            if temp:
                print(temp, "победил!")
                win = True
                break
        if count == 9:
            print("Ничья!")
            break
    image_field(field)

field = list(range(1,10))
main(field)