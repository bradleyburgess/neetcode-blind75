import pytest
from typing import Optional, List, Tuple, Callable
from .solution import Solution, ListNode


def build_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def list_to_array(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


methods: List[Tuple[str, Callable[[Optional[ListNode], int], Optional[ListNode]]]] = [
    ("two_pass", Solution.remove_from_end_two_pass),
    ("floyd", Solution.remove_from_end_floyd),
    ("floyd_dummy", Solution.remove_from_end_floyd_dummy),
]

test_cases: List[Tuple[List[int], int, List[int]]] = [
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1], 1, []),
    ([1, 2], 1, [1]),
    ([1, 2], 2, [2]),
    ([1, 2, 3], 3, [2, 3]),
    ([1, 2, 3], 1, [1, 2]),
    ([1, 2, 3], 2, [1, 3]),
]


@pytest.mark.parametrize("name,method", methods)
@pytest.mark.parametrize("input_list,n,expected", test_cases)
def test_solutions(name, method, input_list, n, expected):
    head = build_list(input_list)
    expected_head = build_list(expected)
    result = method(head, n)
    assert list_to_array(result) == list_to_array(expected_head), (
        f"{name} failed for input {input_list} with n={n}: "
        f"expected {expected}, got {list_to_array(result)}"
    )
