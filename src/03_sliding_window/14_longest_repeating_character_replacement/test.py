import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    ("ABAB", 2, 4),
    ("AABABBA", 1, 4),
    ("AAAA", 2, 4),
    ("ABCDE", 1, 2),
    ("AABABBA", 0, 2),
    ("ABBB", 2, 4),
    ("BAAAB", 2, 5),
    ("ABABABAB", 3, 7),
    ("ABABBAAABBB", 2, 6),
    ("AAABBC", 2, 5),
    ("", 1, 0),
    ("A", 0, 1),
    ("A", 100, 1),
    ("ABCD", 4, 4),
    ("AABBCC", 2, 4),
    ("AABACCA", 2, 5),
    ("ZXYZZX", 1, 3),
    ("XYZXYZ", 3, 5),
    ("BBBBBAAAAACCCCC", 5, 10),
    ("ABCDEABCDEABCDE", 5, 7),
]


methods = [
    ("hash_count_window", Solution.longest_repeating_hash_count_window),
    ("max_freq_window", Solution.longest_repeating_max_freq_window),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("s,k,expected", test_cases)
def test_solutions(name, fn, s, k, expected):
    result = fn(s, k)
    assert result == expected, f"{name} failed for input {s} and {k}"
