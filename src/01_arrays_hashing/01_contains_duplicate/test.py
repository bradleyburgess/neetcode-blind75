import pytest
from .solution import Solution


test_cases = [
    (([1, 2, 3, 1],), True),
    (([1, 2, 3],), False),
    (([],), False),
    (([1],), False),
    (([1, 1],), True),
]


# List of implementations to test
methods = [
    ("brute", Solution.contains_duplicate_brute),
    ("hashmap", Solution.contains_duplicate_hashmap),
    ("sorted", Solution.contains_duplicate_sorted),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("args,expected", test_cases)
def test_valid_anagram_solutions(name, fn, args, expected):
    assert fn(*args) == expected, f"{name} failed for input {args}"
