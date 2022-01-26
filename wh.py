#!/usr/bin/env python3

import argparse


def load_words(word_source):
    """Load the list of 5-letter words from the word list."""
    f = open(word_source, "r")
    # The 5-letter words are len = 6 because of the \n character.
    words = [
        word.strip() for word in f.readlines() if len(word) == 6 and word[0].islower()
    ]
    f.close()
    return words


def filter_for_required_letters(wordlist, required_letters):
    """Filter a list of words for words that contain all of the required letters."""
    filtered_list = [
        word for word in wordlist if all(letter in word for letter in required_letters)
    ]
    return filtered_list


def filter_for_wrong_letters(wordlist, wrong_letters):
    """Filter a list of words for words that don't contain any of the incorrect letters."""
    filtered_list = [
        word for word in wordlist if all(letter not in word for letter in wrong_letters)
    ]
    return filtered_list


def filter_for_known_letters(wordlist, known_letters):
    """Filter a list of words for words that have the known letters in the correct positions."""
    i = 0
    possible_words = wordlist
    for letter in known_letters:
        if letter != "_":
            possible_words = [word for word in possible_words if word[i] == letter]
        i += 1
    return possible_words


def print_list(wordlist):
    """Print the list of matching words."""
    for word in wordlist:
        print(word)
    print(f"{len(wordlist)} possible words.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter possible Wordle solutions.")
    parser.add_argument(
        "-d",
        "--dict",
        dest="word_source",
        type=str,
        help="Specify the path to a list of dictionary words",
        default="/usr/share/dict/words",
    )
    parser.add_argument(
        "-r",
        "--req",
        dest="required_letters",
        type=str,
        help="Specify the letters that are known to be present in the word in a simple string. For example, 'xyz'.",
    )
    parser.add_argument(
        "-w",
        "--wrong",
        dest="wrong_letters",
        type=str,
        help="Specify the letters that are known to be missing in the word in a simple string. For example, 'abc'.",
    )
    parser.add_argument(
        "-k",
        "--known",
        dest="known_letters",
        type=str,
        help="Specify positions of known letters using '_' for missing letters. For example, '_er__'.",
    )
    args = parser.parse_args()

    words = load_words(args.word_source)
    possible_words = words
    if args.required_letters:
        possible_words = filter_for_required_letters(
            possible_words, args.required_letters
        )
    if args.wrong_letters:
        possible_words = filter_for_wrong_letters(possible_words, args.wrong_letters)
    if args.known_letters:
        possible_words = filter_for_known_letters(possible_words, args.known_letters)

    if len(possible_words) > 0:
        print_list(possible_words)
    else:
        print("No words match the conditions.")
