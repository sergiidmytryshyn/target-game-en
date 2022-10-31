from string import ascii_lowercase
from random import choice

def generate_grid():
    """
    () -> list
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    play_field = [[choice(ascii_lowercase) for i in range(3)] for j in range(3)]
    return play_field

grid = generate_grid()
print(grid)
#Creates list of elements from grid to use it in functions.
letters_list = []
for i in grid:
    for j in i:
        letters_list.append(j)
