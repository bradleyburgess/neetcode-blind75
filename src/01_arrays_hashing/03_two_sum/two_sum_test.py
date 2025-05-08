import pytest
from two_sum import two_sum_brute, two_sum_hashmap, two_sum_hashmap_one_pass

test_cases = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
    (([1, 5, 4, 7], 8), [0, 3]),
    (([-1, -2, -3, -4, -5], -8), [2, 4]),
    (([0, 4, 3, 0], 0), [0, 3]),
    (([1, 2, 3, 4, 5], 9), [3, 4]),
    (([10, 20, 40, 50, 60, 70], 50), [0, 2]),
    (([5, 75, 25], 100), [1, 2]),
    (([1, 3, 4, 2], 6), [2, 3]),
    (([5, 5], 10), [0, 1]),
    (([1, 5, 3, 5], 10), [1, 3]),
    (([0, 4, 3, 2], 6), [1, 3]),
    (([80, 20, 40, 10, 30], 70), [2, 4]),
    (([1, 3, 4, 2], 6), [2, 3]),
    (([1, 3, 2, 5, 7], 10), [1, 4]),
]


methods = [
    ("brute", two_sum_brute),
    ("hashmap", two_sum_hashmap),
    ("hashmap_one_pass", two_sum_hashmap_one_pass),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("args,expected", test_cases)
def test_solutions(name, fn, args, expected):
    result = fn(*args)
    assert result == expected, f"{name} failed for input {args}"
    assert result[0] < result[1]
