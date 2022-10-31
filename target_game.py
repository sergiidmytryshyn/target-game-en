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

def get_user_words():
    """
    () -> list
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    users_words = []
    try:
        while True:
            user_input = input("-->")
            users_words.append(user_input)
    except EOFError:
        return users_words

got_user_words = get_user_words()
