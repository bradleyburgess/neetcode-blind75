import pytest
from .solution import Solution
from ..helpers import load_test_cases

test_cases = [
    (tuple(tc["input"]), tc["expected"]) for tc in load_test_cases("03_two_sum")
]


methods = [
    ("brute", Solution.two_sum_brute),
    ("hashmap", Solution.two_sum_hashmap),
    ("hashmap_one_pass", Solution.two_sum_hashmap_one_pass),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("args,expected", test_cases)
def test_solutions(name, fn, args, expected):
    result = fn(*args)
    assert result == expected, f"{name} failed for input {args}"
    assert result[0] < result[1]
