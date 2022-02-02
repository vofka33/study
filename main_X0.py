def intro():
    print()
    print("***********************")
    print(" <<< Х & 0 Game!!! >>> ")
    print("***********************")



def display():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print("x строка, y столбец")
    print()
    print()


def enter_coordinats():
    while True:
        coordinats = input(" >>>  Координаты: ").split()

        if len(coordinats) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = coordinats

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Координаты некорректны, введите числа  ")
            continue

        x, y = int(x), int(y)

        if not (0 <= x <= 2 and 0 <= y <= 2):
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symb = []
        for c in cord:
            symb.append(field[c[0]][c[1]])
        if symb == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symb == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


intro()

field = [[" "] * 3 for i in range(3)]

count = 0

while True:
    count += 1
    display()

    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = enter_coordinats()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break