import pytest
from .solution import Solution

test_cases = [
    (("racecar", "carrace"), True),
    (("jar", "jam"), False),
    (("", ""), True),
    (("a", "a"), True),
    (("a", "b"), False),
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("aabbcc", "abcabc"), True),
    (("abc", "abcd"), False),
    (("Are you alright?", "authorial grey"), True),
    (("lamp", "lamps"), False),
]

methods = [
    ("hashmap", Solution.is_anagram_hashmap),
    ("hashmap_optimized", Solution.is_anagram_hashmap_optimized),
    ("sorted", Solution.is_anagram_sorted),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("args,expected", test_cases)
def test_valid_anagram_solutions(name, fn, args, expected):
    assert fn(*args) == expected, f"{name} failed for input {args}"
