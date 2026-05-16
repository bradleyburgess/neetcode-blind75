from typing import Optional
from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other:
            return False
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )


class Solution:
    @staticmethod
    def invert_recursive(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            Solution.invert_recursive(root.left)
            Solution.invert_recursive(root.right)
        return root

    @staticmethod
    def invert_dfs_stack(root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)

        return root

    @staticmethod
    def invert_bfs_queue(root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.appendleft(root)

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.appendleft(node.left)
                queue.appendleft(node.right)

        return root
