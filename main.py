from typing import List, Tuple
import numpy as np
from matplotlib import pyplot as plt

white = 1
black = 0

FIELD_SIZE = 1024
MIDDLE_POINT = 511

DIRECTIONS = [
    'up',
    'down',
    'right',
    'left',
]
INITIAL_DIRECTION = 'up'

CLOCKWISE = {
    'up': 'right',
    'right': 'down',
    'down': 'left',
    'left': 'up',
}

COUNTERCLOCKWISE = {
    'up': 'left',
    'left': 'down',
    'down': 'right',
    'right': 'up',
}

def invert_position(field: List[List[int]],
                    position: Tuple[int, int]) -> None:
    """
    меняет цвет клетки по месту
    """
    x = position[0]
    y = position[1]
    if field[x][y] == white:
        field[x][y] = black
    else:
        field[x][y] = white


def get_color(field: List[List[int]],
              position: Tuple[int, int]) -> int:
    """
    возвращает цвет клетки по координатам
    """
    x = position[0]
    y = position[1]
    return field[x][y]


def rotate_ant(color: int,
               current_direction: str) -> str:
    """
    Поворачивает муравья в зависимости от цвета, возвращает новое направление
    """
    if color == white:
        return CLOCKWISE[current_direction]
    else:
        return COUNTERCLOCKWISE[current_direction]


def move_ant(position: Tuple[int, int],
             direction: str) -> Tuple[int, int]:
    """
    'Перемещает' муравья - возвращает новую координату
    в зависимости от текущего направления
    """
    x = position[0]
    y = position[1]
    match direction:
        case 'up':
            return (x-1, y)
        case 'left':
            return (x, y-1)
        case 'down':
            return (x+1, y)
        case _:
            return (x, y+1)


def get_ant_way(ant_position: Tuple[int, int],
                ant_direction: str,
                field: List[List[int]]) -> List[List[int]]:
    """
    Возвращает полный путь муравья
    """
    while (ant_position[0] != 0) and (ant_position[0] != FIELD_SIZE - 1) and (ant_position[1] != 0) and (ant_position[1] != FIELD_SIZE - 1):
        color = get_color(field, ant_position)
        ant_direction = rotate_ant(color, ant_direction)
        invert_position(field, ant_position)
        ant_position = move_ant(ant_position, ant_direction)

    return field


def test_get_ant_way():
    """
    Тест пути муравья для поля 7х7
    """
    test_field = [
        [
            1 for row in range(0, 7)
        ] for i in range(0, 7)
    ]
    test_ant_position = (3, 3)
    test_ant_direction = INITIAL_DIRECTION
    test_result = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    test_ant_way = get_ant_way(test_ant_position, test_ant_direction, test_field)
    assert test_ant_way == test_result


def get_way_image(field: List[List[int]]):
    """
    Созраняет изображение пути муравья в файл 'result.png'
    """
    matrix = np.array(field)

    plt.imshow(matrix, cmap='gray')
    plt.show()
    plt.savefig('result.png')


def main():
    prod_field = [
        [
            1 for row in range(0, FIELD_SIZE)
        ] for i in range(0, FIELD_SIZE)
    ]
    ant_position = (MIDDLE_POINT, MIDDLE_POINT)
    ant_direction = INITIAL_DIRECTION

    test_get_ant_way()

    result_field = get_ant_way(ant_position, ant_direction, prod_field)

    get_way_image(result_field)


if __name__ == '__main__':
    main()