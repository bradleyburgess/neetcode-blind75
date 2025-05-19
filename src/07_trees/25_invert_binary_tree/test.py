import pytest
from typing import Optional, List, Callable
from collections import deque
from .solution import Solution, TreeNode

# ---- TreeNode class ----


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


test_cases = [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], []),
    ([1], [1]),
    ([1, 2, None], [1, None, 2]),
]

methods = [
    ("recursive", Solution.invert_recursive),
    ("dfs_stack", Solution.invert_dfs_stack),
    ("bfs_queue", Solution.invert_bfs_queue),
]


@pytest.mark.parametrize("name,fn", methods)
@pytest.mark.parametrize("inputs,expected", test_cases)
def test_invert_tree(
    name: str,
    fn: Callable,
    inputs: List[Optional[int]],
    expected: List[Optional[int]],
):
    root = build_tree(inputs)
    expected = build_tree(expected)
    result = fn(root)
    assert tree_to_list(result) == tree_to_list(
        expected
    ), f"{name} failed for inputs {inputs}"
