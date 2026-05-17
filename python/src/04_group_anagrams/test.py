import pytest

from .solution import Solution
from ..helpers import load_test_cases


# Helper to normalize output (sort groups and contents)
def normalize(result):
    return sorted([sorted(group) for group in result])


test_cases = [
    (tc["input"], tc["expected"]) for tc in load_test_cases("04_group_anagrams")
]

methods = [
    ("sorted", Solution.group_anagrams_sorted),
    ("char_count", Solution.group_anagrams_char_count),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("input_strs,expected", test_cases)
def test_solutions(name, fn, input_strs, expected):
    result = fn(input_strs)
    assert normalize(result) == normalize(
        expected
    ), f"{name} failed for input {input_strs}"
