import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    ("abcabcbb", 3),  # "abc"
    ("bbbbb", 1),  # "b"
    ("pwwkew", 3),  # "wke"
    ("", 0),  # empty string
    ("a", 1),  # single character
    ("au", 2),  # "au"
    ("dvdf", 3),  # "vdf"
    ("abba", 2),  # "ab" or "ba"
    ("tmmzuxt", 5),  # "mzuxt"
    ("anviaj", 5),  # "nviaj"
    ("aabaab!bb", 3),  # "ab!"
    ("abcdefg", 7),  # all unique
]


methods = [
    ("deque_window", Solution.longest_substring_deque_window),
    ("hash_window", Solution.longest_substring_hash_window),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("s,expected", test_cases)
def test_solutions(name, fn, s, expected):
    result = fn(s)
    assert result == expected, f"{name} failed for input {s}"
