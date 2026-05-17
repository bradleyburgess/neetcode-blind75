import pytest
from .solution import Solution
from ..helpers import load_test_cases

test_cases = [
    (tuple(tc["input"]), tc["expected"]) for tc in load_test_cases("02_valid_anagram")
]

methods = [
    ("hashmap", Solution.is_anagram_hashmap),
    ("hashmap_optimized", Solution.is_anagram_hashmap_optimized),
    ("sorted", Solution.is_anagram_sorted),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("args,expected", test_cases)
def test_solutions(name, fn, args, expected):
    assert fn(*args) == expected, f"{name} failed for input {args}"
