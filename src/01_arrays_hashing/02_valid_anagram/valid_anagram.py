"""
--- Helpers ----------------------------------------------------
"""

from enum import Enum
import re


def strip_punctuation(input: str) -> str:
    return re.sub(r"[^a-zA-Z]", "", input).lower()


def increment_letter(hash, letter):
    if letter in hash:
        hash[letter] += 1
    else:
        hash[letter] = 1


class UpdateMode(Enum):
    INCREMENT = "INCREMENT"
    DECREMENT = "DECREMENT"


def update_letter(hash: dict, letter: str, mode: UpdateMode):
    if letter not in hash:
        hash[letter] = 0
    if mode == UpdateMode.INCREMENT:
        hash[letter] += 1
    if mode == UpdateMode.DECREMENT:
        hash[letter] -= 1


"""
--- Solutions --------------------------------------------------
"""


class Solution:
    @staticmethod
    def is_anagram_hashmap(s1: str, s2: str) -> bool:
        hash1 = dict()
        hash2 = dict()
        s1 = strip_punctuation(s1)
        s2 = strip_punctuation(s2)
        for letter in s1:
            increment_letter(hash1, letter)
        for letter in s2:
            increment_letter(hash2, letter)
        return hash1 == hash2

    @staticmethod
    def is_anagram_hashmap_optimized(s1: str, s2: str) -> bool:

        s1 = strip_punctuation(s1)
        s2 = strip_punctuation(s2)
        hash = dict()
        for letter in s1:
            update_letter(hash, letter, UpdateMode.INCREMENT)
        for letter in s2:
            update_letter(hash, letter, UpdateMode.DECREMENT)
        for letter in hash:
            if hash[letter] != 0:
                return False
        return True

    @staticmethod
    def is_anagram_sorted(s1: str, s2: str) -> bool:
        s1 = strip_punctuation(s1)
        s2 = strip_punctuation(s2)
        sorted1 = "".join(sorted(s1))
        sorted2 = "".join(sorted(s2))
        return sorted1 == sorted2
