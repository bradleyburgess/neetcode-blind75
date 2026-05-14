import pytest
from .solution import Solution, ListNode


def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    node = head
    for val in values[1:]:
        node.next = ListNode(val)
        node = node.next
    return head


test_cases = [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
    ([1], [1]),
    ([], []),
]


methods = [
    ("brute", Solution.reverse_linked_list_brute),
    ("optimized", Solution.reverse_linked_list_optimized),
    ("iterative", Solution.reverse_linked_list_iterative),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("input_vals,expected", test_cases)
def test_reverse_linked_list(name, fn, input_vals, expected):
    node = build_linked_list(input_vals)
    result = fn(node)
    assert to_list(result) == expected, f"{name} failed for input {input_vals}"
