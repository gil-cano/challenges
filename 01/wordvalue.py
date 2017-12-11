# -*- coding: utf-8 -*-
from data import DICTIONARY
from data import LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as file:
        return file.read().splitlines()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    # add up all letter values in generator
    return sum(LETTER_SCORES.get(letter.upper(), 0) for letter in word)


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    return max(words, key=lambda w: calc_word_value(w))


if __name__ == "__main__":
    print(max_word_value())
