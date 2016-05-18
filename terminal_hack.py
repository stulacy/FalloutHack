"""
    terminal_hack.py
    ~~~~~~~~~~~~~~~~

    Solves the Mastermind style mini-games to hack security terminals
    in Fallout 3 and New Vegas.
"""

import argparse
import sys
import random
from collections import Counter


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('words', nargs='+')
    args = parser.parse_args()
    return args.words


def letters_in_common(word1, word2):
    return sum(l1 == l2 for l1, l2 in zip(word1, word2))


def mode(x):
    """
    Calculates the most frequently occuring item in a list.
    """
    counts = Counter(x)
    # Magic numbers explained from L-R
    # 1: Get the single most common response as a list of tuples of 
    # (item, count)
    # 0: Get the only tuple from the list
    # 0: Return the modal value itself rather than the count
    return counts.most_common(1)[0][0]


def mean(x):
    """
    Calculates the mean of a list.

    Args:
        x (list): A list with integers or floats.

    Returns:
        The mean of the items as a float.
    """
    return float(sum(x) / len(x))

def get_most_common_word(words):
    """
    Determines the word with the most letters in common with the other words in
    the list.

    Args:
        words (list): List of strings (words)

    Returns:
        An item from the list with the most letters in the same place.
    """
    similarities = [[letters_in_common(w1, w2) for w2 in words if w2 != w1]
                    for w1 in words]
    avg_similarities = [mean(x) for x in similarities]
    # Get word from original list with arg.max of average similarities
    return words[avg_similarities.index(max(avg_similarities))]


def validate_input(words):
    """
    Checks the input words all have the same length.

    Args:
        words (list): A list of strings.

    Returns:
        None, just exits program if error.
    """
    # Assert all words have same length
    lengths = [len(word) for word in words]
    try:
        assert max(lengths) == min(lengths)
    except AssertionError:
        # Find modal value
        modal_length = mode(lengths)
        wrong_lengths = [w for w in words if len(w) != modal_length]
        msg = ("\nUh oh, not all input words are the same length. Check "
               "the following:")
        print(msg)
        for word in wrong_lengths:
            print("'{}'".format(word))
        sys.exit()


def main():
    possibilities = arguments()
    validate_input(possibilities)

    while True:
        # Prompt user to guess word with most letters in common
        guess = get_most_common_word(possibilities)
        print("\nTry '{}'".format(guess))

        while True:
            num_correct = input(("How many letters did this word have"
                                 " correct? (enter 'all' if"
                                 " successful): "))
            try:
                num_correct = int(num_correct)
                break
            except ValueError:
                if num_correct == 'all':
                    print("Password succesfully hacked.")
                    sys.exit()
                print("Please enter an integer!")

        # Since guess wasn't correct remove it from possibilities
        possibilities.remove(guess)
        num_correct = int(num_correct)

        # Reduce possibilities to ones that have this many letters in common
        common = [letters_in_common(guess, w) for w in possibilities]
        possibilities = [word for word, num in zip(possibilities, common) if num == num_correct]

        if len(possibilities) > 1:
            print("{} remaining possibilities".format(len(possibilities)))
        elif len(possibilities) == 1:
            print("\nThe word must be '{}'".format(possibilities[0]))
            break
        else:
            # Should never get here!
            print("\nError! Word should have been determined by now."
                  " Check the spelling of the input words")
            break


if __name__ == "__main__":
    main()
