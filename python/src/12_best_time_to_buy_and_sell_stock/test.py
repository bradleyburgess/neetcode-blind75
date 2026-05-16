import pytest
from .solution import Solution


def normalize(result):
    return sorted(result)


# Format: ([prices], expected_max_profit)

test_cases = [
    ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
    ([7, 6, 4, 3, 1], 0),  # Prices decrease; no profit possible
    ([1, 2, 3, 4, 5], 4),  # Buy at 1, sell at 5
    ([3, 2, 6, 5, 0, 3], 4),  # Buy at 2, sell at 6
    ([2, 4, 1], 2),  # Buy at 2, sell at 4
    ([2, 1, 2, 1, 0, 1, 2], 2),  # Buy at 0, sell at 2
    ([1], 0),  # Only one price; no transaction
    ([], 0),  # Empty list
    ([3, 3, 3, 3, 3], 0),  # No variation; no profit
    ([1, 2], 1),  # Simple increase
    ([2, 4, 1, 7], 6),  # Buy at 1, sell at 7
]


methods = [
    ("brute", Solution.max_profit_brute),
    ("sliding_window", Solution.max_profit_sliding_window),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("prices,expected", test_cases)
def test_solutions(name, fn, prices, expected):
    result = fn(prices)
    assert result == expected, f"{name} failed for input {prices}"
