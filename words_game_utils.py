"""Words game utility functions.

Author: Will Ponczak
Version: 11/7/2023
"""

import random
from colorama import Fore
from nltk.corpus import wordnet as wn


BULL = 2
COW = 1
WRONG = 0


def get_hint(word):
    """Return a hint for this word.

    PART C: use nltk to get a definition for this word.

    Args:
        word (str): the word to find a definition for

    Returns:
        str: a definition or hint for this word
    """
    synonyms = wn.synsets(word)
    definition = synonyms[0].definition()
    return definition


def is_valid_word(word):
    """Check that this word is not a proper noun and a real dictionary word.

    PART C: use nltk to assure this is a regular dictionary word.

    Args:
        word (str): the word to check

    Returns:
        bool: True if this is a valid game word
    """
    if wn.synsets(word):
        return True


def get_random_word(word_dict, length):
    """Select a random word of the selected length.

    Args:
        word_dict (dict): a dict {int:list} where a key is a length,
            and the value is a list of words of that length
        length (int): the desired word length

    Returns:
        str: a random word from the word_dict's list for the given length
    """
    if length in word_dict:
        return random.choice(word_dict[length])
    else:
        return None


def check_guess(secret, guess):
    """Compare the user's guess to the secret word.

    If the guess is the wrong length return None
    Create an empty list, the for each letter in the guess:
        add a 0 (WRONG) if the letter is not in the secret word
        add a 1 (COW) if the letter is in the word but in the wrong position
        add a 2 (BULL) if the letter is in the correct position in the word

    Args:
        secret (str): the secret word being guessed
        guess (str): the current guess

    Returns:
        list: a list of markers, one for each letter
    """
    right_wrong_list = []
    letter = 0
    if len(guess) != len(secret):
        return None
    while letter != len(guess):
        if guess[letter] == secret[letter]:
            right_wrong_list.append(BULL)
        elif guess[letter] != secret[letter]:
            if guess[letter] in secret[0:]:
                right_wrong_list.append(COW)
            else:
                right_wrong_list.append(WRONG)
        letter += 1
            
    return right_wrong_list
        

def color_string(result, guess):
    """Using a result list of letter markers and a guess, print the word in the "Wordle" colors.

    Color scheme:
        red if the letter is not in the secret word
        yellow if the letter is in the word but in the wrong position
        green if the letter is in the correct position in the word
    To assure the resulting string is readable to all users:
        surround green letters with square brackets []
        surround yellow letters with parentheses ()
        leave red letters as is
    For example:
        color_string([1, 0, 2, 1, 0], "PRINT") -> "(P)R[I](N)T"

    Args:
        result (list): the list of letter markers - 0, 1, 2
        guess (str): the current guess

    Returns:
        str: a string where each letter has the right color and is visually marked
    """
    colorstring = ''
    for letter in range(0, len(guess)):
        if result[letter] == 2:
            colorstring += Fore.GREEN + f"[{guess[letter]}]"
        elif result[letter] == 1:
            colorstring += Fore.YELLOW + f"({guess[letter]})"
        elif result[letter] == 0:
            colorstring += Fore.RED + f"{guess[letter]}"
            
    return colorstring


def collection_menu(word_dicts):
    """Create a single string of the word collection names for the user to select from.

        COLLECTIONS
        0    collection_name_0
        1    collection_name_1
        ...
        n    collection_name_n

    Args:
        word_dicts (list): a list of tuples of type (str, dict): a name and a word collection

    Returns:
        str: a string with the given format
    """
    title = 'COLLECTIONS\n'
    q = 0
    for name in word_dicts:
        title += f"{q}:    {name[0]}\n"
        q += 1
        
    return title


if __name__ == "__main__":
    print(get_hint("Lobe"))
    