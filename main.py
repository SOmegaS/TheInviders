# Импорт зависимостей
import sys
import math

# Импорт своих классов
from field import *
from unit import *
from cell import *

# Объявление констант
field_size = 25, 14
hex_size = 60, 70  # Размер гексов (6:7)
screen_size = width, height = field_size[0] * hex_size[0], field_size[1] * hex_size[1]  # Размер экрана


def main():
    # Инициализация
    pg.init()
    screen = pg.display.set_mode(screen_size)
    is_run = True

    # Загрузка данных
    field = Field(screen_size, field_size)
    # field.generate()
    field.gen_given_field()
    unit = Unit(100, 0, 15, 2, 5, 0, 0)
    mouse_x, mouse_y = 0, 0
    while is_run:
        # Обработка событий
        for event in pg.event.get():
            # Выход из игры
            if event.type == pg.QUIT:
                is_run = False

            # Координаты мышки
            if event.type == pg.MOUSEMOTION:
                mouse_x, mouse_y = event.pos

            # Обработка нажатий мышкой
            if event.type == pg.MOUSEBUTTONDOWN:
                # Координаты мышки
                mouse_x, mouse_y = event.pos

                unit.move(mouse_x, mouse_y)

                # Длина от центра юнита до нажатого гекса
                l = int(math.sqrt((mouse_x - unit.x) ** 2 + (mouse_y - unit.y) ** 2))
                # Длина соответствует соседнему гексу из 6
                if hex_size[1] // 2 < l < hex_size[1]:
                    if (mouse_x > unit.x) and (-hex_size[1] // 2 < mouse_y - unit.y < hex_size[1] // 2):  # Вправо
                        unit.x += hex_size[0]
                    elif (mouse_x < unit.x) and (-hex_size[1] // 2 < mouse_y - unit.y < hex_size[1] // 2):  # Влево
                        unit.x -= hex_size[0]
                    elif (0 < mouse_x - unit.x < hex_size[0] // 2) and (mouse_y > unit.y):  # Вправо вниз
                        unit.y += hex_size[1] - hex_size[1] // 4
                        unit.x += hex_size[0] // 2
                    elif (0 < unit.x - mouse_x < hex_size[0] // 2) and (mouse_y > unit.y):  # Влево вниз
                        unit.y += hex_size[1] - hex_size[1] // 4
                        unit.x -= hex_size[0] // 2
                    elif (0 < unit.x - mouse_x < hex_size[0] // 2) and (mouse_y < unit.y):  # Влево вверх
                        unit.y -= hex_size[1] - hex_size[1] // 4
                        unit.x -= hex_size[0] // 2
                    elif (0 < mouse_x - unit.x < hex_size[0] // 2) and (mouse_y < unit.y):  # Вправо вверх
                        unit.y -= hex_size[1] - hex_size[1] // 4
                        unit.x += hex_size[0] // 2

        # Логика работы

        # Отрисовка кадра
        screen.fill((255, 255, 255))  # Белый фон, рисуется первым!
        field.draw(screen)
        unit.draw(screen)
        pg.draw.circle(screen, blue, (mouse_x, mouse_y), 1, 0)

        # Подтверждение отрисовки и ожидание
        pg.display.flip()
        pg.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    main()
