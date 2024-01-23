"""Utility functions for word collections.

Author: Will Ponczak
Version: 11/12/23
"""

from nltk.corpus import wordnet as wn
import words_game_utils as wgu

ALPHABET = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y',
    'Z'
    ]

def check_letters(word):
    """Check each letter in a word to make sure it is in the English alphabet.

    It turns out s.isalpha() accepts characters with umlauts and accent marks,
    which cannot easily be typed on an English keyboard.  Return True if the
    word contains only the letters 'A' through 'Z' and False otherwise.

    Args:
        word(str): the word to check

    Returns:
        bool: True if the word contains only English letters
    """
    for letter in word:
        if letter in ALPHABET:
            return True
        else:
            return False

    


def collect_unique_words(text):
    """Take the text string passed in and produce a set of unique words.

    Split the text into words
    Change every word to uppercase
    Remove all common surrounding punctuation: ().,?!;:#-_'"
    Place the words into a set to remove duplicates, and return

    Args:
        text(str): The text to process

    Returns:
        set: set of unique words from the text
    """
    word_set = set()
    punc = punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for element in text:
        if element in punc:
            new_text = text.replace(element, "")
    split_word = new_text.split(" ") 
    for word in split_word:
        new_word = word.upper()
        word_set.add(new_word)
    #word_set.difference_update(unique_set)
    return word_set
    
    

def clean_word_set(word_set):
    """Take a set of unique words and produce a set of legal words.

    Return a list of the words that have no duplicate letters and contain only letters
    And are considered valid words by nltk

    Args:
        word_set(set): a set of words

    Returns:
        list: list of legal words from the set, all made uppercase
    """
    word_list = []
    for word in word_set:
        if wn.synsets(word):
            new_word = word.upper()
            word_list.append(new_word)
    return word_list


def categorize_words(word_list):
    """Take a list of legal unique words and categorized them by word length into a dictionary.

    Produce a dictionary of the form {int:list} where a key is a word length and its value
    is a list of words of that length, for example:
    {
     2: ['is', 'on', 'at'],
     5: ['value', 'legal', 'words', 'trail']
    }

    Args:
        word_list(list): a list of words

    Returns:
        dict: a dictionary categorized by word length
    """
    word_dict = {}
    for word in word_list:
        if wgu.is_valid_word(word):
            if len(word) in word_dict:
                word_dict[len(word)].append(word)
            else:
                word_dict[len(word)] = [word]
    return word_dict
        
    


if __name__ == "__main__":
    print(categorize_words(['Pool', 'Plumber', 'Trail', 'Six', 'Two']))