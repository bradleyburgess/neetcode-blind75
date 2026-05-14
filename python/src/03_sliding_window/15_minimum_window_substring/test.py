import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("aaflslflsldkalskaaa", "aaa", "aaa"),
    ("ab", "A", ""),  # case-sensitive
    ("abcdebdde", "bde", "deb"),
    ("acbbaca", "aba", "baca"),
    ("", "a", ""),
    # ("a", "", ""),
    ("", "", ""),
    ("abbbbbcdd", "abcd", "abbbbbcd"),
    ("bdab", "ab", "ab"),
    ("bbaac", "aba", "baa"),
    ("ADOBECODEBANCDDD", "ABCD", "BANCD"),
]


methods = [
    ("brute", Solution.minimum_window_brute),
    ("brute_optimized", Solution.minimum_window_brute_optimized),
    ("have_need", Solution.minimum_window_have_need),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("s,t,expected", test_cases)
def test_solutions(name, fn, s, t, expected):
    result = fn(s, t)
    assert result == expected, f"{name} failed for input {s} and {t}"
