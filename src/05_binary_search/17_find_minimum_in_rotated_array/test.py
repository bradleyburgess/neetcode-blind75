import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    ([3, 4, 5, 1, 2], 1),  # rotated, min is in the middle
    ([4, 5, 6, 7, 0, 1, 2], 0),  # rotated, min near the middle
    ([11, 13, 15, 17], 11),  # not rotated
    ([2, 1], 1),  # rotated two-element array
    ([1], 1),  # single element
    ([2, 3, 4, 5, 6, 7, 1], 1),  # min at the end
    ([5, 1, 2, 3, 4], 1),  # min near the beginning
    ([1, 2, 3, 4, 5], 1),  # fully sorted, not rotated
    ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1),  # large rotation
    ([2, 3, 4, 5, 6, 7, 8, 9, 1], 1),  # min at the very end
]


methods = [
    ("verbose_direction", Solution.find_min_verbose_direction),
    ("binary_search", Solution.find_min_binary_search),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("nums,expected", test_cases)
def test_solutions(name, fn, nums, expected):
    result = fn(nums)
    assert result == expected, f"{name} failed for input {nums}"
