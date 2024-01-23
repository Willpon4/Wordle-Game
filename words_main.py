"""The main module of words.

Author: 
"""
import sys
import os
import colorama
import nltk
import words_file_utils as wfu
import words_utils as words_u
import words_game


def process_args(argv):
    """Process the command-line arguments.
    
    Check for the correct number of args. Print the usage statement & then return None if incorrect.
    For each file:
        - If a file does not exist (according to the os module) just skip it with no messages.
        - Use the process_word_file function to make sure each file has the right format and read its text.
        - If a file has the wrong format or no text, just skip it with no messages.
        - Use the collect_unique_words function to process the file's text into a set of unique words.
        - Use the clean_word_set function to process the unique word set into a list of valid words.
        - If there are any words left, use the categorize_words function to put them into a dictionary
        organized by lengths (key is length) and add that dictionary and the word collection title
        to a list of tuples.
    Return the list of tuples - 1 tuple per file that has no errors and contains valid words.
    
    Args:
        args (list): The list of command line arguments
    
    Returns:
        list: a list of tuples, where each tuple contains a str (title of collection),
    """
    tup_list = []
    unique_word_set = set()
    
    if len(argv) < 2:
        print("Usage: python word_main.py file1 [file2 ...]")
        return None
    for filename in argv:
        if os.path.exists(filename) == True:
            with open(filename) as file:
                if wfu.process_word_file(file) is not None:
                    unique_word_set = words_u.collect_unique_words(file)
                    clean_ws = words_u.clean_word_set(unique_word_set)
                    word_dict = words_u.categorize_words(clean_ws)
                    val = (clean_ws[0], word_dict)
                    tup_list.append(val)
    return tup_list
        
            
            
        
        
        
    


if __name__ == "__main__":    
    # Make sure that colorama resets to the default color for your screen when not playing the game
    colorama.init(autoreset=True)
    
    # load the nltk wordnet data
    nltk.download('wordnet')
    
    word_dicts = process_args(sys.argv)
    if word_dicts is None:
        sys.exit(1)
            
    if len(word_dicts) > 0:
        words_game.play_words_game(word_dicts)
    else:
        print("No legal words in these collections.")