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

def get_words(f, letters):
    """
    (str, list) -> list
    Reads the file f. Checks the words with rules and returns a\
    list of words.
    >>> get_words("en.txt", ['h', 'e', 'x', 'o', 'z', 'm', 't', 'y', 'i'])
    ['izote', 'mythize', 'toze', 'zemi', 'zyme', 'zymite', 'zythem']
    """
    with open(f, "r", encoding="utf-8") as file:
        letters_occrances = []
        for let in set(letters):
            letters_occrances.append((let,letters.count(let)))
        words = []
        k = 0
        for line in file:
            k += 1
            line = line.strip().lower()
            checker = True
            checker1 = True
            if k < 3:
                checker = False
            if letters[4] in line and len(line)>=4:
                for b in line:
                    if b not in letters:
                        checker=False
                if checker:
                    for a in letters_occrances:
                        if a[1]<line.count(a[0]):
                            checker1 = False
                    if checker1:
                        words.append(line)
    return words

def get_pure_user_words(user_words, letters, words_from_dict):
    """
    (list, list, list) -> list
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_pure_user_words(['izote', 'hexoz', 'hhexoz'],\
['h', 'e', 'x', 'o', 'z', 'm', 't', 'y', 'i'],\
get_words("en.txt", ['h', 'e', 'x', 'o', 'z', 'm', 't', 'y', 'i']))
    ['hexoz']
    """
    letters_occrances = []
    for let in set(letters):
        letters_occrances.append((let,letters.count(let)))
    pure_words = []
    for word in user_words:
        if (word not in words_from_dict and letters[4] in word
        and len(word)>=4):
            is_pure = True
            for lett in word:
                if lett not in letters:
                    is_pure = False
            for a in letters_occrances:
                if a[1] < word.count(a[0]):
                    is_pure = False
            if is_pure:
                pure_words.append(word)
    return pure_words
