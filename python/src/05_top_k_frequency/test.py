import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


test_cases = [
    (
        [1, 1, 1, 2, 2, 3],
        2,
        [1, 2],
    ),
    (
        [1],
        1,
        [1],
    ),
    (
        [4, 4, 4, 6, 6, 7, 7, 7, 8],
        2,
        [4, 7],
    ),
    (
        [1, 2, 3, 4],
        4,
        [1, 2, 3, 4],
    ),
    (
        [5, 3, 1, 1, 1, 3, 73, 1],
        2,
        [1, 3],
    ),
    (
        [10, 10, 10, 20, 20, 30],
        1,
        [10],
    ),
    (
        [1, 2, 2, 3, 3, 3],
        3,
        [1, 2, 3],
    ),
    (
        [],
        0,
        [],
    ),
]

methods = [
    ("hashmap", Solution.top_k_frequency_hashmap),
    ("heapq", Solution.top_k_frequency_heapq),
    ("buckets", Solution.top_k_frequency_buckets),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("nums,k,expected", test_cases)
def test_solutions(name, fn, nums, k, expected):
    result = fn(nums, k)
    assert sorted(result) == sorted(
        expected
    ), f"{name} failed for input {nums} with k={k}"
