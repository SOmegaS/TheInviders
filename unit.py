import pygame as pg

# Импорт своих классов
from field import *
from cell import *
from main import hex_size

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 180)
red = (255, 0, 0)


# Класс игровых юнитов
class Unit:
    def __init__(self, hp: int, mana: int, dmg: int, moves: int, regen: int, x: int, y: int):
        self.max_hp = hp  # Максимальное количество здоровья
        self.hp = hp  # Здоровье
        self.regen = regen
        self.lvl = 0  # Уровень
        self.exp = 0  # Опыт
        self.max_mana = mana  # Максимальное количество маны
        self.mana = 0  # Количество маны
        self.dmg = dmg  # Урон
        self.max_moves = moves  # Максимальное количество очков перемещения
        self.moves = moves  # Количество очков перемещения
        self.x = x  # Координаты в массиве поля
        self.y = y
        # TODO
        # Сделать подгрузку и отображение

    # Отрисовка юнита
    def draw(self, screen):
        x_pix = 0  # Координаты в пикселях
        y_pix = 0
        if self.x % 2 == 0:
            x_pix = hex_size[0] * self.x + hex_size[0] // 2
            y_pix = 3 * hex_size[1] * self.y // 2 + hex_size[1] // 2
        else:
            x_pix = hex_size[0] * self.x
            y_pix = 3 * hex_size[1] * self.y // 2 + 5 * hex_size[1] // 4
        pg.draw.circle(screen, blue, (x_pix, y_pix), 15, 0)  # Отрисовка

    # Обновление перед ходом
    def refresh(self):
        self.hp += self.regen  # Регенерация
        self.mana = self.max_mana  # Восстановление маны
        self.moves = self.max_moves  # Восстановление очков перемещения

    # Атака
    def attack(self, enemy):
        enemy: Unit
        enemy.hp -= self.dmg  # Нанесение урона
        self.moves = 0  # Обнуление очков перемещения
        if not enemy.is_alive():  # Если противник побежден
            self.exp += 50 // self.lvl ** 0.5  # получение опыта
            self.check()  # Проверка на новый уровень
        else:  # Если противник не побежден
            self.hp -= enemy.dmg // 2  # Нанесение ответного урона
            if not self.is_alive():  # Если юнит погиб
                enemy.exp += 50 // enemy.lvl ** 0.5  # Получение противником опыта
                enemy.check()  # Проверка на новый уровень

    # Проверка на вшивость
    def check(self):
        # Получен ли уровень
        if self.exp >= 100:
            self.lvl += 1
            self.exp = 0

    # Жив ли юнит
    def is_alive(self):
        return self.hp > 0

    # Можно ли ходить
    def movement(self):
        return self.moves > 0

    # Ход
    def move(self, mouse_x: int, mouse_y: int):
        # Проверка на координаты гекса
        i = j = k = 0
        # Верхняя левая и нижняя правая линии
        while mouse_y > (i + 1) * hex_size[1] // 2 - 2 * mouse_x // 3 + 2 * hex_size[1] // 7:
            i += 1
        # Верхняя правая и нижняя левая линии
        while mouse_y > (j + 1) * hex_size[1] // 2 + 2 * mouse_x // 3 - 2 * hex_size[1] // 7:
            j += 1
        # Левая и правая линии
        while mouse_x > hex_size[0] * (k + 1) // 2:
            k += 1
        print(f'({mouse_x}; {mouse_y}): {i}, {j}, {k}')
