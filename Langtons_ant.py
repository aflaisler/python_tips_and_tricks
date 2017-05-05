from memory_profiler import profile
from collections import deque
import numpy as np
import pandas as pd

# Next change the zeros to ones!


# direction
def get_direction(direction, case_color=0):
    """
    return the direction at the next step
    """
    dir_1 = {0: 1, 1: 2, 2: 3, 3: 0}
    dir_0 = {v: k for k, v in dir_1.iteritems()}
    if case_color:
        return dir_1[direction]
        # position
    else:
        return dir_0[direction]


get_direction(0, case_color=1)


def next_position(t0=(0, 0), case_color=1, direction=0, X=[1, 1], Y=[1, 1]):
    """
    ti is a tuple with coordonate (ie.: (x, y))
    """
    move_l = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    move_r = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}
    # rotation of referentiel relative to direction of mouse
    d = get_direction(direction, case_color)
    # ref = d - 3 if d - 3 >= 0 else d + 1
    if case_color:
        move = move_r[direction]
    else:
        move = move_l[direction]
    l = zip(t0, move)
    # scale measurement
    X[0] = min(X[0], X[0] + move[0])
    X[1] = max(X[1], X[0] + move[0])
    Y[0] = min(Y[0], Y[0] + move[1])
    Y[1] = max(Y[1], Y[1] + move[1])
    return tuple([sum(x) for x in l]), d


# step 1
new_position, d = next_position(
    t0=(0, 0), case_color=1, direction=0, X=[1, 1], Y=[1, 1])
old_grid = [[1]]
X = [1, 1]
Y = [1, 1]
get_grid(old_grid, new_position, d, X, Y)
# step 2
new_position, d = next_position(
    t0=(1, 0), case_color=0, direction=1, X=[1, 2], Y=[1, 1])
old_grid = [[1, 0]]
X = [1, 2]
Y = [1, 1]
old_grid = get_grid(old_grid, new_position, d, X, Y)
# step 3
new_position, d = next_position(
    t0=(1, 1), case_color=1, direction=0, X=[1, 2], Y=[1, 2])
get_grid(old_grid, new_position, d, X, Y)


def get_grid(old_grid, new_position, direction, X, Y):
    pos = new_position
    sh = np.shape(old_grid)
    if (new_position[0] == X[0]) and (direction == 3):
        lst_ = np.zeros(shape=(sh[0], 1), dtype=int)
        new_grid = np.concatenate((lst_, old_grid), axis=1)
        return new_grid
    elif (new_position[0] == X[1]) and (direction == 1):
        lst_ = np.zeros(shape=(sh[0], 1), dtype=int)
        new_grid = np.concatenate((old_grid, lst_), axis=1)
        return new_grid
    elif (new_position[1] == Y[0]) and (direction == 2):
        lst_ = np.zeros(shape=(1, sh[1]), dtype=int)
        new_grid = np.concatenate((old_grid, lst_), axis=0)
        return new_grid
    elif (new_position[1] == Y[1]) and (direction == 0):
        lst_ = np.zeros(shape=(1, sh[1]), dtype=int)
        new_grid = np.concatenate((lst_, old_grid), axis=0)
        return new_grid
    else:
        print "do nothing"


def moves(iterations):
    for i in iterations:


old_grid = [[1, 1]]
next_position(t0=(1, 1), case_color=0, direction=0)
ant([[1]], 0, 0, 3, 0)


def ant(grid, column, row, n, direction=0):
