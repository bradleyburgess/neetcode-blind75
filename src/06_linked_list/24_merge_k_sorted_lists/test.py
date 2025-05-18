from .solution import Solution, ListNode

from typing import Optional, List
import pytest


def list_to_linked(lst: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# -
test_cases = [
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([[], []], []),
    ([], []),
    ([[1], [0]], [0, 1]),
    ([[1, 3, 5], [2, 4, 6], [0, 7, 8]], [0, 1, 2, 3, 4, 5, 6, 7, 8]),
    ([[5, 10], [1, 2, 3]], [1, 2, 3, 5, 10]),
]


methods = [
    ("priority_queue", Solution.merge_k_sorted_priority_queue),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("lists,expected", test_cases)
def test_solution(name, fn, lists, expected):
    linked_inputs = [list_to_linked(lst) for lst in lists]
    result = fn(linked_inputs)
    assert linked_to_list(result) == expected, f"{name} failed for inputs {lists}"
