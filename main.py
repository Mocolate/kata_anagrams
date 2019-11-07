from typing import List


def read_word_list(filename: str = 'wordlist.txt') -> List[str]:
    word_list = [line.rstrip('\n') for line in open(filename)]

    return word_list


# Write your code here!
