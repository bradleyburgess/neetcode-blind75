import pytest
from longest_consecutive_sequence import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    # Basic cases
    ([100, 4, 200, 1, 3, 2], 4),  # Sequence: 1, 2, 3, 4
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),  # Sequence: 0 to 8
    ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),  # Sequence: -1 to 5
    # Duplicates
    ([1, 2, 0, 1], 3),  # Sequence: 0, 1, 2
    # Negative numbers
    ([0, -1], 2),  # Sequence: -1, 0
    ([-3, -2, -1, 0, 1], 5),  # Sequence: -3 to 1
    # Minimal / edge cases
    ([1], 1),  # Single element
    ([], 0),  # Empty list
    ([1, 2, 3, 4, 5], 5),  # Already sorted sequence
    ([10, 30, 20, 40], 1),  # No consecutive numbers
    # Repeated long runs
    ([1, 9, 3, 10, 4, 20, 2], 4),  # Sequence: 1, 2, 3, 4
    ([5, 2, 99, 3, 4, 1, 100], 5),  # Sequence: 1, 2, 3, 4, 5
    # Large gaps between elements
    ([0, 100, 200, 300], 1),
]

methods = [
    ("brute", Solution.longest_consecutive_brute),
    ("one_pass", Solution.longest_consecutive_chain_start),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("nums,expected", test_cases)
def test_solution(name, fn, nums, expected):
    result = fn(nums)
    assert result == expected, f"{name} failed for input {nums}"
