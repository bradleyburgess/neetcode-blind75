from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node: {self.val} -> {self.next}" if self.next else f"Node: {self.val}"


class Solution:
    @staticmethod
    def detect_loop_set(head: Optional[ListNode]) -> bool:
        if not head:
            return False
        ids = set()
        node = head
        while node:
            node_id = id(node)
            if node_id in ids:
                return True
            ids.add(node_id)
            node = node.next

        return False

    @staticmethod
    def detect_loop_floyd(head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
        
        return False
