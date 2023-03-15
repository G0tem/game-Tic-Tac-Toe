from random import choice


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self._win = 0  # 0 игра, 1 чел, 2 комп, 3 ничья

    def __getitem__(self, item):
        x, y = item
        try:
            self.pole[x][y]
        except:
            raise IndexError('некорректно указанные индексы')

        return self.pole[x][y].value

    def __setitem__(self, key, value):
        x, y = key
        try:
            self.pole[x][y]
        except:
            raise IndexError('некорректно указанные индексы')

        if bool(self.pole[x][y]) == False:
            raise ValueError('клетка уже занята')

        self.pole[x][y].value = value

        self.__win_status()

    def __win_status(self):
        for row in self.pole:  # Проверка по строкам
            if all(x.value == self.HUMAN_X for x in row):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self._win = 2
                return

        for i in range(3):  # Проверка по колонкам
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self._win = 2
                return

        if all(self.pole[i][i].value == self.HUMAN_X for i in range(3)) or \
                all(self.pole[i][-1-i].value == self.HUMAN_X for i in range(3)):  # Проверка по диагоналям
            self._win = 1
            return

        if all(self.pole[i][-1-i].value == self.COMPUTER_O for i in range(3)) or \
                all(self.pole[i][i].value == self.COMPUTER_O for i in range(3)):  # Проверка по диагоналям
            self._win = 2
            return

        if all(x.value != self.FREE_CELL for row in self.pole for x in row):  # Если все занято
            self._win = 3

    def init(self):
        self.__init__()

    def show(self):
        for r in self.pole:
            for j in r:
                print(j.value, end=" ")
            print()
        print('__________________________________________')

    def human_go(self):
        coor = input('Введите координаты хода в формате: "11" - центр: ')
        x, y = int(coor[0]), int(coor[1])
        game[x, y] = self.HUMAN_X

    def sv_kletki(self):
        res = []
        for i in range(3):
            for j in range(3):
                if bool(self.pole[i][j]):
                    res.append(str(i) + str(j))
        return res

    def computer_go(self):
        zero = self.sv_kletki()
        c = choice(zero)
        x, y = int(c[0]), int(c[1])
        game[x, y] = self.COMPUTER_O

    @property
    def is_human_win(self):
        return self._win == 1

    @property
    def is_computer_win(self):
        return self._win == 2

    @property
    def is_draw(self):
        return self._win == 3

    def __bool__(self):
        return self._win == 0 and self._win not in (1, 2, 3)

class Cell:

    def __init__(self):
        self.value = 0  # 0-свободно; 1-X; 2-0

    def __bool__(self):
        return self.value == 0


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")