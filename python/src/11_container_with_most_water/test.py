import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    # Basic cases
    ([1, 1], 1),
    ([1, 2, 1], 2),
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    # Symmetric case
    ([2, 3, 4, 5, 18, 17, 6], 17),
    # Decreasing heights
    ([5, 4, 3, 2, 1], 6),  # between 5 and 2
    # Increasing heights
    ([1, 2, 3, 4, 5], 6),  # between 1 and 5
    # Plateaus
    ([4, 4, 4, 4, 4], 16),
    # Peaks in middle
    ([1, 3, 2, 5, 25, 24, 5], 24),
    # Two tall bars with smaller ones in between
    ([1, 2, 4, 3, 4, 1], 8),
    # Tallest bars at ends
    ([6, 1, 2, 3, 4, 5, 6], 36),
    # Edge case: single height (should never happen in valid input)
    # ([5], ?)  # Problem requires at least two lines
    ([5], 0),
]


methods = [
    ("brute", Solution.container_most_water_brute),
    ("two_pointer", Solution.container_most_water_two_pointer),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("heights,expected", test_cases)
def test_solutions(name, fn, heights, expected):
    result = fn(heights)
    assert result == expected, f"{name} failed for input {heights}"
