"""File utility functions.

Author: Will Ponczak
Version: 11/10/23
"""


def process_word_file(filename):
    """Read the file, check its correctness and return the word collection name and its data.

    This file has the following format: The first line must contain the word WORDS
    followed by a space, and the rest of the first line is interpreted as the name
    for this collection of words. The following lines in the file can be in any format,
    for example:
            WORDS War and Peace
            ...
            the text of the book War and Peace
            ...

    If any of the following errors occur, the function should return None:
        The file does not have "WORDS" as the first word on the first line
        The file does not contain a name for the word collection on the 1st line
        The rest of the file is empty
    If there are no errors, the function should return a tuple of 2 items:
        the name of the word collection in a single string
        the word collection in a single string

    Args:
        filename (str): The name of the file to read from

    Returns:
        str: The name to use for this collection of words
        str: The rest of the file in a single string
        None: if any of the errors occur
    """
    with open(filename) as file:
        f_line = file.readline()
        words = f_line.split(' ')
        if words[0] != 'WORDS' or len(words) <= 1:
            return None
        contents = file.read()
        if len(contents) == 0:
            return None
        name = f_line[6:(len(f_line) - 1)]
        
    return name, contents
    