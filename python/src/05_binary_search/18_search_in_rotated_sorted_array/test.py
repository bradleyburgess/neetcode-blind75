import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    # Simple cases
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1),
    ([1], 1, 0),
    # No rotation
    ([1, 2, 3, 4, 5, 6, 7], 4, 3),
    ([1, 2, 3, 4, 5, 6, 7], 8, -1),
    # Full rotation (same as no rotation)
    ([1, 2, 3, 4, 5, 6, 7], 7, 6),
    # Rotation in the middle
    ([6, 7, 1, 2, 3, 4, 5], 3, 4),
    ([6, 7, 1, 2, 3, 4, 5], 6, 0),
    ([6, 7, 1, 2, 3, 4, 5], 5, 6),
    # Target at pivot
    ([5, 6, 7, 1, 2, 3, 4], 1, 3),
    ([5, 6, 7, 1, 2, 3, 4], 5, 0),
    # Large array with rotation
    (list(range(30, 101)) + list(range(0, 30)), 10, 81),
    (list(range(30, 101)) + list(range(0, 30)), 29, 100),
    (list(range(30, 101)) + list(range(0, 30)), 100, 70),
    (list(range(30, 101)) + list(range(0, 30)), 101, -1),
    # Edge cases
    ([], 5, -1),
    ([1, 3], 3, 1),
    ([3, 1], 3, 0),
]


methods = [
    ("binary_search", Solution.find_in_rotated_binary_search),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("nums,target,expected", test_cases)
def test_solutions(name, fn, nums, target, expected):
    result = fn(nums, target)
    assert result == expected, f"{name} failed for input {nums} and {target}"
