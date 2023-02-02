from random import randint as ri
import time

digit = [x for x in range(10)]
field = [[" " for i in range(10)] for x in range(10)]
fired = []
victory = False


def draw_field(field):
  print(" ", *digit)
  for i in range(10):
    print(i, end=' ')
    for j in range(10):
      print(field[i][j], end=' ')
    print()


def fill_field(field, fire, fill):
  x, y = fire[0], fire[1]
  field[x][y] = fill


def input_fire(fired):  #ввод координат
  while True:  # цикл для правильного  ввода числа
    try:  # попытка получить целое число с клавиатуры
      z = input("Введите координаты выстрела: ")  # ввод числа
      if len(z) == 2: # Поверка что введено 2 числа
        if int(z): 
          x, y = list(z)
          break  # выход из цикла если  попытка успешна
      else:
        print("Вводите 2 только цифры!")
    except ValueError:  # Ошибка получения целого числа с клавиатуры
      print("Вводите только цифры!")  # подсказка пользователю
  return int(x), int(y)  # возврат функцией введенного целого числа


def gen_ships():  # генерация кораблей
  list_ships = [4, 3, 3, 2, 1]  # список кораблей с числом клеток
  ships = []  # список кораблей
  used_cells = set()  # занятые поля

  for cell in list_ships:  # перебираем корабли из списка
    while True:
      ship = set()
      d = ri(0, 1)  #X or Y
      if d == 0:  # X
        initX = ri(0, 9 - cell)
        initY = ri(0, 9)
        minX = initX - 1
        maxX = initX + cell
        minY = initY - 1
        maxY = initY + 1
        for j in range(cell):
          ship.add((initX + j, initY))

      else:
        initX = ri(0, 9)
        initY = ri(0, 9 - cell)
        minX = initX - 1
        maxX = initX + 1
        minY = initY - 1
        maxY = initY + cell
        for j in range(cell):
          ship.add((initX, initY + j))

      if used_cells & set(ship) == set():
        ships.append(ship)  #добавляем корабль в список
        break

    for k in range(minX, maxX + 1):
      for l in range(minY, maxY + 1):
        if -1 < k < 10 and -1 < l < 10:
          used_cells.add((k, l))

  # отладка
  '''
  for i in used_cells:
    fill_field(field, i, '.')

  for ship in ships:
    for i in ship:
      fill_field(field, i, 'X')
  '''
  return ships


def chec_fire(ships, fired, fire):
  if fire not in fired:
    fired.append(fire)
    chk = '.'
    for ship in ships:
      for cell in ship:
        if fire == cell:
          ship.remove(cell)
          chk = "Х"
          if len(ship) == 0:
            chk = "~"
            del ship
            ships.remove(set())
          break
      fill_field(field, fire, chk)
  else:
    print("В это поле уже стреляли")
    time.sleep(1.5)
  return fired

#Игра
squadron = gen_ships()
draw_field(field)
#print(squadron)
while victory == False:

  fire = input_fire(fired)
  fired = chec_fire(squadron, fired, fire)
  print("\033[H\033[J")
  draw_field(field)
  if squadron == []:
    victory = True
print("Вы победили!")
print(f"Вам потребовалось {len(fired)} выстрелов")
