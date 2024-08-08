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

def invert_position(field, position):
    x = position[0]
    y = position[1]
    if field[x][y] == white:
        field[x][y] = black
    else:
        field[x][y] = white

def get_color(position):
    x = position[0]
    y = position[1]
    return field[x][y]

def rotate_ant(color, current_direction):
    if color == white:
        return CLOCKWISE[current_direction]
    else:
        return COUNTERCLOCKWISE[current_direction]

def move_ant(position, direction):
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
    
field = [
    [
        1 for row in range(0, FIELD_SIZE)
    ] for i in range(0, FIELD_SIZE)
]

def main():
    ant_position = (MIDDLE_POINT, MIDDLE_POINT)
    ant_direction = INITIAL_DIRECTION

    while (ant_position[0] != 0) and (ant_position[0] != FIELD_SIZE - 1) and (ant_position[1] != 0) and (ant_position[1] != FIELD_SIZE - 1):
        color = get_color(ant_position)
        ant_direction = rotate_ant(color, ant_direction)
        invert_position(field, ant_position)
        ant_position = move_ant(ant_position, ant_direction)

    # for row in field:
    #     print(row)

    matrix = np.array(field)

    plt.imshow(matrix, cmap='gray')
    plt.show()
    plt.savefig('result.png')

if __name__ == '__main__':
  main()