import pytest
from .solution import Solution
from ..helpers import load_test_cases

test_cases = [
    ((tc["input"],), tc["expected"]) for tc in load_test_cases("01_contains_duplicate")
]

# List of implementations to test
methods = [
    ("brute", Solution.contains_duplicate_brute),
    ("hashmap", Solution.contains_duplicate_hashmap),
    ("sorted", Solution.contains_duplicate_sorted),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("args,expected", test_cases)
def test_solutions(name, fn, args, expected):
    assert fn(*args) == expected, f"{name} failed for input {args}"
