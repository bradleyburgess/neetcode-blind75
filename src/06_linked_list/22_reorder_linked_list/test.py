import pytest
from typing import List, Optional, Tuple, Callable
from .solution import Solution, ListNode


# Helpers
def list_to_linked_list(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for val in items[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def clone_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    dummy = ListNode(0)
    current_new = dummy
    current_old = head
    while current_old:
        current_new.next = ListNode(current_old.val)
        current_new = current_new.next
        current_old = current_old.next
    return dummy.next


# Test cases in (input list, expected reordered list)
test_cases: List[Tuple[List[int], List[int]]] = [
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 3, 2]),
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ([10, 20, 30, 40], [10, 40, 20, 30]),
    (
        [1, 100, 2, 99, 3, 98],
        [1, 98, 100, 3, 2, 99],
    ),  # not valid input for reorderList, but tests arbitrary inputs
]


methods: List[Tuple[str, Callable[[Optional[ListNode]], None]]] = [
    ("pairs", Solution.reorder_list_pairs),
    ("floyd", Solution.reorder_list_floyd),
    ("floyd_simpler", Solution.reorder_list_floyd_simpler),
]


@pytest.mark.parametrize("name,method", methods)
@pytest.mark.parametrize("input_list,expected_list", test_cases)
def test_reorder_list(
    name: str,
    method: Callable[[Optional[ListNode]], None],
    input_list: List[int],
    expected_list: List[int],
):
    head = list_to_linked_list(input_list)
    method(
        clone := clone_linked_list(head)
    )  # use a clone in case of method mutating input
    result = linked_list_to_list(clone)
    assert (
        result == expected_list
    ), f"{name} failed for input {input_list}. Got {result}, expected {expected_list}"
