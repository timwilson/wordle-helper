#!/usr/bin/env python3


def load_words():
    f = open("/usr/share/dict/words", "r")
    words = [
        word.strip() for word in f.readlines() if len(word) == 6 and word[0].islower()
    ]
    f.close()
    return words


def filter_for_required_letters(wordlist, required_letters):
    filtered_list = [
        word for word in wordlist if all(letter in word for letter in required_letters)
    ]
    return filtered_list


def filter_for_wrong_letters(wordlist, wrong_letters):
    filtered_list = [
        word for word in wordlist if all(letter not in word for letter in wrong_letters)
    ]
    return filtered_list


if __name__ == "__main__":
    words = load_words()
