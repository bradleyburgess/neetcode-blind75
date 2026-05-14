import pytest
from .solution import ListNode, Solution


def build_linked_list(values, pos=-1):
    """
    Build a linked list from a list of values. If `pos` is not -1,
    a cycle is introduced connecting the last node to the node at index `pos`.
    """
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


# List of test cases: (values, pos), expected
test_cases = [
    (([3, 2, 0, -4], 1), True),  # Cycle connects to node at index 1
    (([1, 2], 0), True),  # Cycle connects to head
    (([1], -1), False),  # Single node, no cycle
    (([1], 0), True),  # Single node pointing to itself
    (([], -1), False),  # Empty list
    (([1, 2, 3, 4, 5], -1), False),  # No cycle
]


# Methods to test
methods = [("set", Solution.detect_loop_set), ("floyd", Solution.detect_loop_floyd)]


@pytest.mark.parametrize("name,method", methods)
@pytest.mark.parametrize("inputs,expected", test_cases)
def test_solution(name, method, inputs, expected):
    head = build_linked_list(*inputs)
    assert method(head) == expected, f"{name} failed for inputs {inputs}"
