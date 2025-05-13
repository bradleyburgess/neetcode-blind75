import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    # Basic test with multiple valid triplets
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    # All zeros – only one triplet
    ([0, 0, 0, 0], [[0, 0, 0]]),
    # No valid triplets
    ([1, 2, -2, -1], []),
    # Duplicates that shouldn't be counted multiple times
    ([-1, -1, -1, 2, 2], [[-1, -1, 2]]),
    # Larger range with multiple valid combinations
    ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
    # Negative numbers only
    ([-5, -4, -3, -2, -1], []),
    # Positive numbers only
    ([1, 2, 3, 4, 5], []),
    # Edge case: fewer than 3 elements
    ([1, 2], []),
    ([], []),
    # Triplets involving both ends of the list
    (
        [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
        [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
    ),
]


methods = [
    ("brute", Solution.three_sum_brute),
    ("two_pointers", Solution.three_sum_two_pointers),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("nums,expected", test_cases)
def test_solutions(name, fn, nums, expected):
    result = fn(nums)
    assert normalize(result) == normalize(expected), f"{name} failed for input {nums}"
