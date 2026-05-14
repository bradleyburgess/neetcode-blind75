import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([2, 3, 4, 5], [60, 40, 30, 24]),
    ([1, 0, 3, 4], [0, 12, 0, 0]),
    ([0, 0, 3, 4], [0, 0, 0, 0]),
    ([5], [1]),
    ([1, -1], [-1, 1]),
    ([-1, -2, -3, -4], [-24, -12, -8, -6]),
    ([9, 0], [0, 9]),
    ([0, 1], [1, 0]),
    ([3, 3, 3], [9, 9, 9]),
    ([1, 2, 3, 0, 4], [0, 0, 0, 24, 0]),
    ([10, 5, 2], [10, 20, 50]),
    ([100, 1, 1, 1], [1, 100, 100, 100]),
    ([], []),
]


methods = [
    ("zero_index", Solution.product_except_self_zero_index),
    ("prefix_suffix", Solution.product_except_self_prefix_suffix),
    ("prefix_suffix_optimized", Solution.product_except_self_prefix_suffix_optimized),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("nums,expected", test_cases)
def test_solutions(name, fn, nums, expected):
    result = fn(nums)
    assert result == expected, f"{name} failed for input {nums}"
