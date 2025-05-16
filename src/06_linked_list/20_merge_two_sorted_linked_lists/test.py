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
    (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
    (([], []), []),
    (([], [0]), [0]),
    (([5], [1, 2, 3]), [1, 2, 3, 5]),
]


@pytest.mark.parametrize("inputs,expected", test_cases)
def test_solution(inputs, expected):
    l1 = build_linked_list(inputs[0])
    l2 = build_linked_list(inputs[1])
    result = Solution.merge_sorted_linked_lists(l1, l2)
    assert to_list(result) == expected
