""" Analyzes the word frequencies in a book downloaded from


Project Gutenberg """

import string
import random
import math
from random import randint
import requests

herland_full_text = requests.get('http://www.gutenberg.org/files/32/32-0.txt').text
#print(herland_full_text)


def get_word_list(herland_full_text):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    # exclude = set(string.punctuation)
    # exclude = set()
    # s1 = ''.join(ch for ch in s1 if ch not in exclude)
    herland_text = str(herland_full_text)

    #print(herland_text)
    #print(type(herland_text))

    herland_text.index('CHAPTER 1')
    #print(lines)
    #print(type(start_book))
    for c in herland_text:
        #print(c)
        if c in set(string.punctuation):

            book = herland_text.replace(c,"")

            book = book.strip()
            #print(book)
    # print(lines)

    #make all letters lowercase
    book = str.lower(book)

    whole_text = book

    word_list = whole_text.split(' ')
    return word_list
#print(word_list)



def get_top_n_words(x, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    new_dict = {}


    for word in x:
        if word not in new_dict:
            new_dict[word] = 1
            #new_dict[word] = index + 1
        else:
            new_dict[word] = new_dict[word] + 1
            #new_dict[word].append(word_list[index+1])
    #print(new_dict)

    ordered_by_frequency = sorted(new_dict.keys(), key=new_dict.get, reverse=True)
    #print(ordered_by_frequency)
    top = ordered_by_frequency[:n]
    print(top)
    return top

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    #print(string.punctuation)
    wl = get_word_list(herland_full_text)
    get_top_n_words(wl, 3)
