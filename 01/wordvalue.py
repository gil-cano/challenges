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
    value = 0
    for letter in word:
        value += LETTER_SCORES.get(letter.upper(), 0)
    return value


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    max_word = ''
    max = 0
    for word in words:
        word_value = calc_word_value(word)
        if word_value > max:
            max_word = word
            max = word_value
    return max_word


if __name__ == "__main__":
    print(max_word_value())
